from flask import Flask
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
    
def Error404(error):
    return '<h1>Contacte a soporte tecnico</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, Error404)
    app.run()
