from flask import Flask,render_template
app = Flask(__name__)

from dbconnect import connection
from wtforms import Form, BooleanField, TextField, PasswordField, validators

@app.route("/")
def hello():
    return render_template("main.html")
    
@app.route("/g3-tesis-experience/")
def g3tesis():
    return render_template("main.html")   
 

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])

   
@app.route("/register_page/",methods=["GET","POST"])
def register_page():
    try:
        c,conn=connection()
        return("okay")
    except Exception as e :
        return(str(e))
    
if __name__ == "__main__":
    app.debug=True
    app.run()
