import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from reportlab.pdfgen import canvas
from io import BytesIO
import mysql.connector
import datetime

def crear_pdf(nombre, fecha_nacimiento):
    # Crear un archivo PDF con el nombre y fecha de cumpleaños
    today = datetime.date.today()
    if today.month == fecha_nacimiento.month and today.day == fecha_nacimiento.day:
        mensaje = f"Feliz cumpleaños, {nombre}!\n\n¡Te deseamos un día maravilloso!"
        packet = BytesIO()
        c = canvas.Canvas(packet)
        c.drawString(100, 750, mensaje)
        c.save()
        packet.seek(0)
        return packet
    else:
        return None

def enviar_correo(destinatario, asunto, mensaje, pdf_attachment):
    remitente = "udgcorreos115@gmail.com"  # Reemplaza con tu dirección de correo
    contraseña = "mtzy zsdn vwnx jwdx"  # Reemplaza con tu contraseña (o utiliza variables de entorno)

    # Configuración del servidor de correo
    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login(remitente, contraseña)

    # Creación del correo
    correo = MIMEMultipart()
    correo['From'] = remitente
    correo['To'] = destinatario
    correo['Subject'] = asunto

    # Adjuntar el PDF al correo si existe
    if pdf_attachment:
        pdf_filename = "mensaje.pdf"
        pdf_attachment = MIMEBase('application', 'octet-stream')
        pdf_attachment.set_payload(pdf_attachment.read())
        encoders.encode_base64(pdf_attachment)
        pdf_attachment.add_header('Content-Disposition', f'attachment; filename={pdf_filename}')
        correo.attach(pdf_attachment)

    # Enviar el correo
    servidor.send_message(correo)
    servidor.quit()

def main():
    # Conectarse a la base de datos
    conexion = mysql.connector.connect(
        host="tu_host",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
    cursor = conexion.cursor(dictionary=True)

    # Obtener la fecha actual
    today = datetime.date.today()

    # Consulta para obtener profesores con cumpleaños hoy
    consulta = f"SELECT nombre, fecha_nacimiento, correo FROM profesores WHERE DAY(fecha_nacimiento) = {today.day} AND MONTH(fecha_nacimiento) = {today.month}"
    cursor.execute(consulta)

    for profesor in cursor:
        nombre = profesor['nombre']
        fecha_nacimiento = profesor['fecha_nacimiento']
        correo = profesor['correo']
        pdf_attachment = crear_pdf(nombre, fecha_nacimiento)

        if pdf_attachment:
            # Enviar correo de felicitación
            asunto = f"Feliz cumpleaños, {nombre}!"
            mensaje = f"Feliz cumpleaños, {nombre}!\n\n¡Te deseamos un día maravilloso!"
            enviar_correo(correo, asunto, mensaje, pdf_attachment)

    cursor.close()
    conexion.close()

if __name__ == "__main":
    main()

