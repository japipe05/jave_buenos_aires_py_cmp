from flask import render_template,request
from database.cassandra.conexion import session
from models.login import verify_password

def principalindex():
    username = request.form['username']
    password = request.form['password']
    
    if username and password:
        query = "SELECT credencial FROM users WHERE usuario=%s"
        result = session.execute(query, [username])
        
        if result:
            if verify_password(result, password):
                return render_template('index.html')
        return "Invalid username or password"
    return "Invalid request"



    