# Departamentos y municipios de Bolivia
# Descripción 
Web scraping para obtener los departamentos de Bolivia con sus municipios actuales
## Tabla de contenido
- [Requerimientos](#requerimientos)
- [Advertencia](#advertencia)
- [Clone repo](#clone-repo)
- [Configuración](#configuración)
    - [Crear un entorno virtual](#crear-un-entorno-virtual)
    - [Variables de entorno](#variables-de-entorno)
- [Ejecutar](#ejecutar)

## Requerimientos
- Python
- Google chrome
- PostgreSQL
## Advertencia

En caso de que la pagina web https://www.municipio.com.bo tenga cambios drásticos el script puede no funcionar correctamente

## Clone repo

```bash
git clone https://github.com/rogerramosruiz/deparatamentos-bolivia.git
cd deparatamentos-bolivia
```

## Configuración

### Crear un entorno virtual

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Variables de entorno

Windows

```powershell
move .env.sample .env
```

Cambiar POSTGRESDB_URL acorde a su base de datos en .env

## Ejecutar

```bash
python main.py
```