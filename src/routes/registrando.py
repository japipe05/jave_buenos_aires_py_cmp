from flask import render_template, request
from database.cassandra.conexion import session
from models.login import hash_password

def principalregistro():
    username = request.form['username']
    telefono = request.form['telefono']
    password = request.form['password']

    Usejave = hash_password(password).hex()
    session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', '"+username+"')")
    session.execute("INSERT INTO topicos.users (credencial, usuario) VALUES ('"+Usejave+"', '"+telefono+"')")

    return render_template('login.html')