import smtplib , ssl
import os

def send_message(message):
    host = "smtp.gmail.com"

    port= 465

    username = "shrijeetkumarverma140504@gmail.com"

    password= os.getenv("PASSWORD_PORTFOLIO_WEBAPP")

    reciever = "shrijeetkumarverma140504@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server :
        server.login(username , password)
        server.sendmail(username , reciever , message)
        
