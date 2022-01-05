def send_email(error_mail):
    import smtplib

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('exampleabc@gmail.com', 'notarealpassword')
    server.sendmail('exampleabc@gmail.com','user@abc.com',error_mail)
