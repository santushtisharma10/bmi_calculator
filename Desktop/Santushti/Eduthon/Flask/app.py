from flask import Flask, render_template, request, redirect, url_for
import smtplib
import cv2
import pytesseract
import os
from googlesearch import search

print("module imported")

app = Flask(__name__, template_folder='template')
print("Success")

def sendmail(name, reas):

    obj = smtplib.SMTP("smtp.gmail.com", 587)

    obj.starttls()

    obj.login("sharmasantushti1012", "aryan@130614")

    subject = "Sending email via python script"
    body = "Hi " + name +" I am sending this email using python script. I am sending it because "+reas
    
    message = "Subject: {}\n\n{}".format(subject, body)

    sender = "sharmasantushti1012"
    receiver = ["nareshsharma2503@gmail.com"]

    obj.sendmail(sender, receiver, message)

    obj.quit()

    print("Success")

def textdet(name) :
    
    img = cv2.imread(name)
#img = cv2.resize(img, (1180, 780))

    #cv2.waitKey(0)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    str1 = pytesseract.image_to_string(img)

    print(str1)
    
    #os.remove(name)
    
    return str1
    #cv2.imshow("img", img)
    #cv2.waitKey(0)

#print("Success")

def srch(str) :
    lis = []
    query = str
    for j in search(query, tld ="com", lang='en', num =10, stop = 10, pause=2.0):

        lis.append(j)
    return lis

@app.route("/" )
def index():
    return render_template("index1.html")

@app.route("/2", methods = ['POST', 'GET'])
def pg():
    if request.method == 'POST':
        name = request.form['nm']
        reas = request.form['r']
        sendmail(name, reas)
        return redirect('/2')
    else :
        return render_template("2.html")

@app.route("/3", methods = ['POST', 'GET'])
def nxt():
    lis = []
    if request.method == 'POST':
        name = request.files['file']
        #text = textdet(name)
        name.save(os.path.join("C:/Users/Hp/Desktop/Santushti/Eduthon/Flask",name.filename))
        text = textdet(name.filename)
        lis = srch(text)
        print(lis)
        value = 1
        return render_template("3.html", lis = lis)

    else :
        return render_template("3.html", lis = lis)

if __name__ == "__main__":
    app.run(debug = True)