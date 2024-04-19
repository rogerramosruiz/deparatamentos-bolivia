from selenium import webdriver
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.chrome.options import Options
from loadDB import load_data_to_db

def getDepartamentos(url:str):
    br.get(url)
    departamentos_table = br.find_element(By.CLASS_NAME, 'reg_br').find_elements(By.TAG_NAME, 'a')
    departamentos_url = [(a.text, a.get_attribute('href')) for a in departamentos_table]
    return departamentos_url

def getMunicipios(url:str):
    br.get(url)    
    municipos_table = br.find_element(By.CLASS_NAME, 'annuaire').find_elements(By.TAG_NAME, 'a')
    municipios = [a.text for a in municipos_table]
    try:
        pages_table = br.find_element(By.ID, 'div_webpage').find_element(By.TAG_NAME, 'table')
        nextUrl = pages_table.find_element(By.CLASS_NAME, "next").get_attribute('href')
        municipios += getMunicipios(nextUrl)
    except Exception:
        pass
    return municipios

def get_data(url:str):
    data = {}
    depratamntos = getDepartamentos(url)
    for i in depratamntos:
        data[i[0]] = getMunicipios(i[1])
    return data

def save_data_json(file_name: str, data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f,  ensure_ascii=False)

def main():
    data = get_data(url)
    save_data_json('departamentos.json', data)
    load_data_to_db(data)

if __name__ == '__main__':
    url = 'https://www.municipio.com.bo/'
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--start-maximized")
    br = webdriver.Chrome(options=options)
    main()