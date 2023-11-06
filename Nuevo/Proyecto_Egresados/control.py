from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#from Nuevo.Proyecto_Egresados.control import model

app = Flask(__name__)
mysql=MySQL(app)

@app.route('/general', methods=['GET','POST'])
def general():
     return render_template('Generales.html')
     if request.method == 'POST':
          nombre_gen = request.form['nombres']
          apellido_p = request.form['apellido_p']
          apellido_m = request.form['apellido_m']
          sexo = request.form['sexo']
          telefono = request.form['tel_contacto']
          correo = request.form['correo_alumno']
          c_postal = request.form['codigo_postal']
          pais = request.form['pais']
          estado = request.form['estado']
          ciudad = request.form['ciudad']
          colonia = request.form['colonia']
          nacionalidad = request.form['nacionalidad']
          f_nacimiento = request.form['f_nacimiento']
          print('Datos generales guardados')

@app.route('/estudios', methods=['GET', 'POST'])
def estudios():
     return render_template('Estudios.html')
     if request.method == 'POST':
          nivel_estudios = request.form['nivel']
          carrera = request.form['carrera']
          titulado = request.form['titulado']
          ciclo = request.form['ciclo']
          ingles = request.form['ingles']
          promedio = request.full_path['promedio']
          print('Datos estudiantiles guardados')

@app.route('/laboral', methods=['GET','POST'])
def add_registro():
     return render_template('Laboral.html')
     if request.method == 'POST':
         lugar= request.form['lugardetrabajo']
         horario= request.form['horariolaboral']
         puesto= request.form['puestolaboral']
         siOno = request.form['trabajasiono']
         print('Datos laborales guardados')






@app.route('/dashboard')
def dashboard():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM info_laboral")
    data = cursor.fetchall()
    cursor.close()
    return render_template('dashboard.html', data=data)


@app.route('/inicio')
def inicio():
     return render_template('inicio.html')

@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/seleccion')
def seleccion():
     return render_template('seleccion.html')

@app.route('/dash')
def dash():
     return render_template('dashboard.html')

def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'
