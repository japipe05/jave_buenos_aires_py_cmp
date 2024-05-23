from flask import render_template, request
from database.cassandra.conexion import session
from models.login import verify_password
from models.login import hash_password

def registro():
    #console.log("hello")
    return render_template('registro.html')
    