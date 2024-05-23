from flask import render_template,request
def login():

    print("credenciales")
    return render_template('login.html')