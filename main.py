from flask import Flask

# Nueva instancia de Flask
# __name__ = Nombre del archivo
app = Flask(__name__)

@app.route('/')
def hello():
    var = 'Hola mundo'
    return var
