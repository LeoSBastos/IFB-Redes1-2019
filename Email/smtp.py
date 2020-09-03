import smtplib
import time
sender = "Private Person <from@smtp.mailtrap.io>"
receiver = "FDS <leosbastos7@gmail.com>"




with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    # for i in range(10):
    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}

    This is a test e-mail message."""

    server.login("725229b7001390", "9aed9ab8f6ed8e")
    server.sendmail(sender, receiver, message)
        # time.sleep(10)