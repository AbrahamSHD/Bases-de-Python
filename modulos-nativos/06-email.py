from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

mensaje = MIMEMultipart()
mensaje["from"] = "Hola Mundo"
mensaje["to"] = "abraham82514456@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del msj", "plain")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    # * Identificarnos
    smtp.ehlo()
    # * Encriptar datos
    smtp.starttls()

    smtp.login("correo", "contraseña")
    smtp.send_message(mensaje)
