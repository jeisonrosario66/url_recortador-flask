import sqlite3
import random
import string
import re
from flask_bootstrap import Bootstrap
from flask import flash
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from hashids import Hashids

def get_db_connection():
    """Ejecuta conexion con la base de datos

    Returns:
        conex: conexion con base de datos
    """
    #Apunta hacia la ubicacion de la base de datos
    conex = sqlite3.connect("db/database.db")
    conex.row_factory = sqlite3.Row
    #retorna la conexion
    return conex

#Instancia de la app flask
app = Flask(__name__)

#Genera una cadena aletoria
random_KEY = ''.join(random.choice(string.printable) for i in range(30))
app.config["SECRET_KEY"] = random_KEY

#A partir de 'SECRET_KEY' se generara otro hash aletorio
#Dicho hash servida para identificar el link recotado
hashids = Hashids(min_length=4, salt=app.config["SECRET_KEY"])

# Nueva instancia de Bootstrap
bootstrap = Bootstrap(app)

#Ruta index acepta 2 metodos 
@app.route("/", methods=("GET", "POST"))
def index():
    
    #Experecion regular para validar que es un url valida
    forma_url = re.compile('^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$')
    conex = get_db_connection()

    #Si me metodo es post
    if request.method == "POST":
        #Almace la url enviada en 'url'
        url = request.form["url"]
        
        if not url:
            #Si en envia la url vacia
            flash("La URL es requerida")
            return redirect(url_for("index"))

        elif forma_url.search(url) == None:
            flash("Esta URL no tiene un formato valido")
            flash("Formato valido esperado: 'https:ejemplo.com'")
            
            return redirect(url_for("index"))
        
        #Insert en base de datos
        url_data = conex.execute("INSERT INTO urls (url_original) VALUES (?)", (url,))
        conex.commit()
        conex.close()

        #almacena la ID de la URL
        #lastrowid: proporciona el ID de fila de la última fila insertada.
        url_id = url_data.lastrowid
        
        #Construye un hash usando el hashids.encode()
        #hashids.encode(1) | salida ej: 'KJ34'
        hashid = hashids.encode(url_id)
        
        #Construye la URL corta usando request.host_url
        #request.host_url: Objeto para accecder a la url del host
        #Resultado http://127.0.0.1:5000/KJ34
        short_url = request.host_url + hashid

        return render_template("index.html", short_url=short_url)

    return render_template("index.html")

#Ruta de redireccionamiento
@app.route("/<id>")
def url_redirect(id):
    conex = get_db_connection()

    #decode() método de la hashids, convierte el hash a su valor entero original y almacenarlo en el original_id
    original_id = hashids.decode(id)
    if original_id:
        original_id = original_id[0]
        url_data = conex.execute(
            "SELECT url_original, clicks FROM urls" " WHERE id = (?)", (original_id,)
        ).fetchone()
        original_url = url_data["url_original"]
        clicks = url_data["clicks"]

        conex.execute(
            "UPDATE urls SET clicks = ? WHERE id = ?", (clicks + 1, original_id)
        )

        conex.commit()
        conex.close()
        return redirect(original_url)
    else:
        flash("URL Invalido")
        return redirect(url_for("index"))


@app.route("/stats")
def stats():
    conex = get_db_connection()
    db_urls = conex.execute(
        "SELECT id, creado, url_original, clicks FROM urls"
    ).fetchall()
    conex.close()

    urls = []
    for url in db_urls:
        url = dict(url)
        url["short_url"] = request.host_url + hashids.encode(url["id"])
        urls.append(url)

    return render_template("stats.html", urls=urls)