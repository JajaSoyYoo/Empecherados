from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

global nombre_gen, apellido_p, apellido_m, sexo, telefono, correo, c_postal, pais, estado, ciudad, colonia, nacionalidad, f_nacimiento
global uni_proce, carrera, titulado, ciclo, ingles, promedio

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
          insertGeneral(nombre_gen, apellido_p, apellido_m, sexo, telefono, correo, c_postal, pais, estado, ciudad, colonia, nacionalidad, f_nacimiento)
          return redirect(url_for('estudios'))
    
    return render_template('Generales.html')
          

@app.route('/estudios', methods=['GET', 'POST'])
def estudios():
    if request.method == 'POST':
          uni_proce = request.form['nivel']
          carrera = request.form['carrera']
          titulado = request.form['titulado']
          ciclo = request.form['ciclo']
          ingles = request.form['ingles']
          promedio = request.form['promedio']
          insertEstudios(uni_proce, carrera, titulado, ciclo, ingles, promedio, correo)
          return redirect(url_for('laboral'))

    return render_template('Estudios.html')

@app.route('/laboral', methods=['GET','POST'])
def laboral():
    if request.method == 'POST':
         lugar= request.form['lugardetrabajo']
         horario= request.form['horariolaboral']
         puesto= request.form['puestolaboral']
         siOno = request.form['trabajasiono']
         sector = request.form['sector']
         #insertGeneral(nombre_gen, apellido_p, apellido_m, sexo, telefono, correo, c_postal, pais, estado, ciudad, colonia, nacionalidad, f_nacimiento)
         #insertEstudios(uni_proce, carrera, titulado, ciclo, ingles, promedio)
         insertLaboral(lugar, horario, puesto, siOno, sector, correo)
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

@app.route('/seleccion', methods=['GET', 'POST'])
def seleccion():
     if request.method == 'POST': 
          return redirect(url_for('general'))
          
     return render_template('seleccion.html')


def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'


def insertGeneral(nombre_gen, apellido_p, apellido_m, sexo, telefono, correo, c_postal, pais, estado, ciudad, colonia, nacionalidad, f_nacimiento):
     cursor = mysql.connection.cursor()
     cursor.execute("insert into general (Nombres, Apellido_P, Apellido_M, Sexo, Tel_Contacto, Correo_ALumno, Codigo_Postal, Pais, Estado, Ciudad, Colonia, Nacionalidad, F_Nacimiento) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (nombre_gen, apellido_p, apellido_m, sexo, telefono, correo, c_postal, pais, estado, ciudad, colonia, nacionalidad, f_nacimiento))
     mysql.connection.commit()
     cursor.close()
     mysql.connection.close()

def insertEstudios(uni_proce, carrera, titulado, ciclo, ingles, promedio, correo):
     cursor = mysql.connection.cursor()
     cursor.execute("insert into grado_estudios values(%s, %s, %s, %s, %s, %s, %s);", (uni_proce, carrera, titulado, ciclo, ingles, promedio, correo))
     mysql.connection.commit()
     cursor.close()
     mysql.connection.close()

def insertLaboral(lugar, horario, puesto, siOno, sector):
     cursor = mysql.connection.cursor()
     cursor.execute("insert into info_laboral values(%s, %s, %s, %s, %s, %s, %s);", (siOno, lugar, horario, puesto, sector, correo))
     mysql.connection.commit()
     cursor.close()
     mysql.connection.close()
