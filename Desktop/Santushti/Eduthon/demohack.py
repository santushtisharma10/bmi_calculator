import smtplib

obj = smtplib.SMTP("smtp.gmail.com", 587)

obj.starttls()

obj.login("sharmasantushti1012", "aryan@130614")

subject = "Sending email via python script"
body = "Hi I am sending this email using python script. Reply with a message on whatsapp if you received it"

message = "Subject: {}\n\n{}".format(subject, body)

sender = "sharmasantushti1012"
receiver = ["syedareehaquasar@gmail.com", "kashikajain3101@gmail.com"]

obj.sendmail(sender, receiver, message)

obj.quit()

print("Success")