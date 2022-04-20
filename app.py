from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
from Funciones import consultar
import pymysql

app = Flask(__name__)
app.secret_key = 'Ponganos_100_profe_:('

@app.route('/')
def index():
    if 'logged_in' in session.keys():
        if session['logged_in'] == True:
          return render_template("index.html")
    else:
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
            if usuario_correcto == True:
                session['username'] = username
                session['nombre'] = name
                session['logged_in'] = True
                return redirect('/')
            else:
                msg = f'Usuario o contraseña incorrectos.'
                return render_template("login.html", mensaje=msg)

@app.route('/agendar_cita', methods=['GET', 'POST'])
def crear_cita():
    if request.method == 'GET':
        return render_template("cita.html")
    else:
        if request.method == 'POST':
            return redirect('/')


@app.route('/historial/')
@app.route('/historial/recetas', methods=['GET'])
def historial_recetas():
    if request.method == 'GET':
        return render_template('recetas.html')


@app.route('/historial/atencion', methods=['GET'])
def historial_atencion():
    if request.method == 'GET':
        return render_template('atencion.html')

if __name__ == '__main__':
    app.run(debug=True)
