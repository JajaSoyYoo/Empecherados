import mysql.connector # se debe descargar la libreria "pip install mysql-connector-python
import datos
conexion = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "1234",
    db = "seg_egresados",
)

cursor = conexion.cursor()

correo = datos.correo
contra = datos.contra

cursor.execute("insert into usuarios (correo, contraseña) values ('" + correo + "' ,'" + contra + "')")
conexion.commit()

cursor.execute("select * from usuarios")
for bd in cursor:  # type: ignore
    print(bd)