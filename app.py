from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
from Funciones import consultar
import pymysql

app = Flask(__name__)
loggeado = False

@app.route('/')
def index():
    if loggeado == True:
        return render_template("index.html")
    else:
        if loggeado == False:
            return redirect('./login')

@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    if request.method == 'GET':
        return render_template("login.html")
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            lista = consultar(username, password)
            username=lista[0]
            name=lista[1]
            usuario_correcto = lista[2]
            print(username)
            print(name)
            print(usuario_correcto)
            if usuario_correcto == True:
                session['username'] = username
                session['nombre'] = name
                session['logged_in'] = True
                loggeado = True
                return redirect('/', loggeado)
            else:
                msg = f'Usuario o contraseña incorrectos.'
                return render_template("login.html", mensaje=msg)



if __name__ == '__main__':
    app.run(debug=True)
