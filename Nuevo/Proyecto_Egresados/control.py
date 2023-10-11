from flask import Flask, render_template, request
from flask_mysqldb import MySQL
#from Nuevo.Proyecto_Egresados.control import model

app = Flask(__name__)
mysql=MySQL(app)

@app.route('/Registro_Laboral')
def laboral():
     return render_template('Laboral.html')

@app.route('/laboral', methods=['POST'])
def add_registro():
     if request.method == 'POST':
         lugar= request.form['lugardetrabajo']
         horario= request.form['horariolaboral']
         puesto= request.form['puestolaboral']
         siOno = request.form['trabajasiono']
         cursor = mysql.connection.cursor()
         cursor.execute("insert into info_laboral (Trabajando, Direccion_trabajo, Horario_Laboral, Puesto_Trabajo, Correo_PK_Info) values ('"+siOno+"', '"+lugar+"', '"+horario+"', '"+puesto+"','alan.hcris@gmail.com')")
         mysql.connection.commit()
         return general()

@app.route('/General')
def general():
     return render_template('Generales.html')



@app.route('/inicio')
def inicio():
     return render_template('inicio.html')

@app.route('/seleccion')
def seleccion():
     return render_template('seleccion.html')

@app.route('/dash')
def dash():
     return render_template('dashboard.html')

def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'