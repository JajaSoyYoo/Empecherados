import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Crear una base de datos SQLite para almacenar información de profesores
def crear_base_de_datos():
    conn = sqlite3.connect('profesores.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS profesores
                      (nombre TEXT, fecha_nacimiento TEXT)''')

    conn.commit()
    conn.close()

# Agregar un profesor a la base de datos
def agregar_profesor(nombre, fecha_nacimiento):
    conn = sqlite3.connect('profesores.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO profesores VALUES (?, ?)", (nombre, fecha_nacimiento))

    conn.commit()
    conn.close()

# Enviar correos de cumpleaños
def enviar_correo_cumpleanios(destinatario, nombre, fecha_nacimiento):
    hoy = datetime.now()
    fecha_actual = hoy.strftime("%Y-%m-%d")

    if fecha_nacimiento == fecha_actual:
        remitente = "udgcorreos115@gmail.com"
        contraseña = "mtzy zsdn vwnx jwdx"  # Recuerda no incluir contraseñas en texto claro en tu código

        # Configuración del servidor de correo
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)

        # Creación del correo
        correo = MIMEMultipart()
        correo['From'] = remitente
        correo['To'] = destinatario
        correo['Subject'] = "¡Feliz Cumpleaños!"

        # Mensaje de felicitación
        mensaje = f"¡Feliz Cumpleaños, {nombre}! Esperamos que tengas un día maravilloso."
        correo.attach(MIMEText(mensaje, 'plain'))

        # Enviar el correo
        servidor.send_message(correo)
        servidor.quit()

# Uso de las funciones
# Crear la base de datos
crear_base_de_datos()

# Agregar profesores (nombre, fecha de nacimiento) a la base de datos
agregar_profesor("Profesor 1", "2023-10-28")
agregar_profesor("Profesor 2", "2000-05-15")

# Enviar correos de cumpleaños si es el cumpleaños del profesor
enviar_correo_cumpleanios("correo_profesor1@gmail.com", "Profesor 1", "2023-10-28")
enviar_correo_cumpleanios("correo_profesor2@gmail.com", "Profesor 2", "2000-05-15")
