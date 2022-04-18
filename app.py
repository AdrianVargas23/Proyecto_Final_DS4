from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
from Funciones import consultar
import pymysql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if request.method == 'POST':
            username = request.form['username']
            print(username)
            password = request.form['password']
            print(password)
            consultar(username, password)
            username=usuario
            name=nombre
            usuario_correcto = check
            print(username)
            print(name)
            print(usuario_correcto)
            if usuario_correcto == True:
                session['username'] = username
                session['nombre'] = name
                session['logged_in'] = True
                return redirect('/')
            else:
                msg = f'Usuario o contraseña incorrectos.'
                return render_template("login.html", mensaje=msg)



if __name__ == '__main__':
    app.run(debug=True)
