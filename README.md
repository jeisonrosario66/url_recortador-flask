
# URL recortador flask

Web App Capaz de tomar un link y devolver una versión recortada

Construido con `Flask`

![app](https://github.com/jeisonrosario66/flask-guia/assets/96961824/01ba77ed-55b4-473c-8bac-e3bafbc1d1e5)

![app 2](https://github.com/jeisonrosario66/flask-guia/assets/96961824/2d20fdcf-730b-426c-8707-db2c35affbca)

## Ejecutar

```bash
$ git clone https://github.com/jeisonrosario66/url_recortador-flask
$ cd url_recortador-flask
$ pip install -r requirements.txt
$ flask run
```

#### Antes de Ejecutar**
Si intenta ejecutar el proyecto sin unos requerimientos necesarios previos, Lo mas probable es que obtengo errores.

* Requerimientos (En orden de prioridad)
    - establecer variables de entorno
    - Entorno virtual
    - Dependencias
    - Crear base de datos
    - Ejecutar
### Variables de entorno

```bash
$ export FLASK_APP=main.py
```

Estas son opcional, para hacer debug al código
```bash
$ export FLASK_DEBUG=1
$ export FLASK_ENV=development
```
### Entorno virtual
Lo mas recomendable es ejecutar el proyecto en un entorno virtual con `python3.9`

Se recomienda usar `virtualenv` o `venv`

Desde el entorno virtual instalar las dependencias requeridas `pip install -r requirements.txt`

### Crear base de datos
La base de datos debe ser creada con los siguiente comando
```bash
$ cd db
$ python init_db.py
```
No obtendrá ninguna salida

Sin embargo puede verificar su archivo en `db/database.db`

#### Importante 
`init_db.py` Cada que se ejecuta verifica que no exista la base de datos `database.db` y si existe la ELIMINA, por ello debe ser ejecutado solo 1 vez

### Ejecute 
Ahora si, no debería obtener ningún error al ejecutar la app `$ flask run`

![server on](https://github.com/jeisonrosario66/flask-guia/assets/96961824/4b46cfd6-fbd7-4e6d-8070-f5eb6de795da)

## Tests de pruebas

Para correr los Tests corra el siguiente comando desde la raíz del proyecto

```bash
  $ pre-commit run --all-files
```

![test](https://github.com/jeisonrosario66/flask-guia/assets/96961824/0aadb5c1-f074-4c7a-89d6-c4057c99d594)

*****Puede esperar una salida como esta*****


## Soporte

Para soporte, email developer@jeisonrosariodev.com 
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](http://jeisonrosariodev.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jeison-rosario-0488a7253/)



## Autor

- [@jeisonrosario66](https://github.com/jeisonrosario66)

