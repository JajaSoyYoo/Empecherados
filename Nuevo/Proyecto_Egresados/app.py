from flask import Flask, render_template, request
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)
mysql=MySQL(app)

@app.route('/')
def jalar():
#    try:
        cursor = mysql.connection.cursor()
        sql = "delete from cordis"
        cursor.execute(sql)
        mysql.connection.commit()
        return 'cordis actualizado'
#    except Exception as ex:
#        return "Error"

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

@app.route('/Estudios')
def estudios():
     return render_template('Estudios.html')

@app.route('/inicio')
def inicio():
     return render_template('inicio.html')

@app.route('/seleccion')
def seleccion():
     return render_template('seleccion.html')


def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, Error404)
    app.run()
