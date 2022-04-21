from flask import Flask, render_template, request, redirect, session
from passlib.hash import sha256_crypt
from Funciones import consultar
from insertar import insertar
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
            contrasenia_verificada = lista[2]
            if contrasenia_verificada == True:
                session['username'] = username
                session['nombre'] = name
                session['logged_in'] = True
                return redirect('/')
            else:
                msg = f'Usuario o contraseña incorrectos.'
                return render_template("login.html", mensaje=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            firs_name = request.form['first_name']
            last_name = request.form['last_name']
            phone = request.form['phone']
            pregunta = request.form['pregunta']
            respuesta = sha256_crypt.hash(request.form['respuesta'])
            lista = insertar(username, password, firs_name, last_name, phone, pregunta, respuesta)
            usuario = lista[0]
            nombre = lista[1]
            contrasenia_verificada = lista[2]
            if contrasenia_verificada == True:
                session['username'] = usuario
                session['nombre'] = nombre
                session['logged_in'] = True
                return redirect('/')
            else:
                msg = f'Usuario o contraseña incorrectos.'
                return render_template("register.html", mensaje=msg)


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
