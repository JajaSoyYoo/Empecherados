from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL


#from Nuevo.Proyecto_Egresados.control import model

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'
mysql=MySQL(app)

@app.route('/general', methods=['GET', 'POST'])
def general():
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
          print(telefono)
          return redirect(url_for('estudios'))
    
    return render_template('Generales.html')
          

@app.route('/estudios', methods=['GET', 'POST'])
def estudios():
    if request.method == 'POST':
          nivel_estudios = request.form['nivel']
          carrera = request.form['carrera']
          titulado = request.form['titulado']
          ciclo = request.form['ciclo']
          ingles = request.form['ingles']
          promedio = request.form['promedio']
          print('Datos estudiantiles guardados')
          return redirect(url_for('laboral'))

    return render_template('Estudios.html')

@app.route('/laboral', methods=['GET','POST'])
def laboral():
    if request.method == 'POST':
         lugar= request.form['lugardetrabajo']
         horario= request.form['horariolaboral']
         puesto= request.form['puestolaboral']
         siOno = request.form['trabajasiono']
         print('Datos laborales guardados')

         return redirect(url_for('inicio'))
    
    return render_template('Laboral.html')


#@app.before_request
#def before_request():
#    if 'user_id' not in session and request.endpoint != 'login':
#        flash('Debes iniciar sesión para acceder a esta página.', 'warning')
#        return redirect(url_for('login'))

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contra = request.form['contra']

        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM cordis WHERE Correo_Cordinador = %s AND contra = %s", (correo, contra))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Autenticación exitosa, establecer una sesión para el usuario.
            session['user_id'] = user[0]  # Accede al primer valor en la tupla (Correo_Cordinador)
            return redirect(url_for('dashboard'))
        else:
            # Autenticación fallida
            flash('Credenciales incorrectas. Por favor, inténtalo de nuevo.', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/seleccion')
def seleccion():
     return render_template('seleccion.html')


def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'
