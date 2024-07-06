import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


path = Path("image.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Hola mundo"
mensaje["to"] = "andemar@hotmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() # Identificarnos
    smtp.starttls() # Transport Layer Security
    smtp.login("email@gmail.com", "passEmail")
    smtp.send_message(mensaje)
    print("Mensaje enviado!")