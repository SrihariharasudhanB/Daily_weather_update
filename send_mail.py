import smtplib
from email.message import EmailMessage

class Mail:
    def __init__(self) -> None:
        pass

    def sendMail(self,message):

        message = "Coimbatore - Weather:\n\n"+message
        mail = EmailMessage()
        mail['Subject'] = "Daily Weather Update!"
        mail['From'] = "< FROM ID >"
        mail['To'] = "< TO ID >"
        mail.set_content(message)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("< MAILING ID >","< MAIL ID PASSWORD >")
        server.send_message(mail)
        server.close()
