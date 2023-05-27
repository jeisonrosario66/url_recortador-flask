# inicializar la base de datos (Solo se requiere una vez)
import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())

connection.commit()
connection.close()
