from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Munanwosu1@localhost/ismsdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import models

@app.route("/")
def home():
    return '''My name is Munachimso Nwosu. This is my CA2 work. 
    My GitHub URL is https://github.com/NwosuMunachimso'''

@app.route("/home/")
def home2():
    return render_template('home.html', title= 'Home')

@app.route("/register/")
def registeruser():
    return render_template('register.html')

@app.route("/register/")
def registereduser():
    return render_template('registeredUsers.html')

@app.route("/process-signup/", methods=['POST'])
def process_signup():
# Let's get the request object and the parameters sent.
    firstname = request.form['firstname']
    surname = request.form['surname']
    dateofbirth = request.form['dateofbirth']
    residentialaddress= request.form['residentialaddress']
    nationality = request.form['nationality']
    nationalidentificationnumber= request.form['nationalidentificationnumber']
# let's write to the database
    try:
        user = models.User(firstname=firstname, surname=surname,  dateofbirth=dateofbirth, residentialaddress=residentialaddress,nationality=nationality,nationalidentificationnumber=nationalidentificationnumber)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
# Error caught, prepare error information for return
        information = 'Could not submit. The error message is {}'.format(e.__cause__)
        return render_template('signup.html', title="SIGN-UP", information=information)
# Let us prepare success feedback information
    information = 'User by name {} {} successfully added. The login name is the email address {}.'.format(firstname, surname, nationalidentificationnumber)
    return render_template('signup.html', title="SIGN-UP", information=information)


if __name__ == "__main__":
    app.run(port=5005)