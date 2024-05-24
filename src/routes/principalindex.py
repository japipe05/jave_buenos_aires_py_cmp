from flask import render_template, request
from database.cassandra.conexion import session
from models.login import verify_password

def principalindex():
    username = request.form['username']
    password = request.form['password']
    
    if username and password:
        query = "SELECT credencial FROM users WHERE usuario=%s"
        result = session.execute(query, [username])
        
        if result and verify_password(result, password):
            return render_template('home.html')
        else:
            error = "Invalidad credenciales"
            return render_template('error.html', error=error)
    error = "Invalid request"
    return render_template('error.html', error=error)
