import json
import psycopg
from conf import POSTGRESDB_URL

def craete_tables(cursor):
    create_tables_query = '''
    DROP TABLE IF EXISTS municipio;
    DROP TABLE IF EXISTS departamento;
    CREATE TABLE departamento(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        nombre VARCHAR(50) UNIQUE
    );
    CREATE TABLE municipio(
        id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        nombre VARCHAR(50),
        id_departamento INT REFERENCES departamento(id)
    );
    '''
    cursor.execute(create_tables_query)


def make_query_municipios(municipios, id_departamento:int):
    values = []
    for municipio in municipios:
        values.append(f"('{municipio.title()}', {id_departamento})")

    return 'INSERT INTO municipio(nombre, id_departamento) VALUES ' + ', '.join(values)
    

def insert_departamento(departamento:str, cursor):
    insert_departamento_query = 'INSERT INTO departamento(nombre) values (%s) returning id'
    cursor.execute(insert_departamento_query, (departamento,))
    return cursor.fetchone()[0]



def insert_data(data, cursor):
    for departamento, municipios in data.items():
        id_departamento = insert_departamento(departamento, cursor)
        municipios_query = make_query_municipios(municipios, id_departamento)
        cursor.execute(municipios_query)

def load_data_to_db(data):
    with  psycopg.connect(POSTGRESDB_URL) as connection:
        with connection.cursor() as cursor:
            craete_tables(cursor)
            insert_data(data, cursor)
            connection.commit()
    
if __name__ == '__main___':
    data = json.load(open("departamentos.json"))
    load_data_to_db(data)