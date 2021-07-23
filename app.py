#!/usr/bin/python3.7

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, static_folder="resources", template_folder='template')

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://zabwrkyozaflpj:79f109a4b2723480a6868026193c4c5e95e2c685a64c8ceb559f9128b24057d2@ec2-54-173-31-84.compute-1.amazonaws.com:5432/dd8hjc23082m92"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(30))
    phone = db.Column(db.BigInteger)
    email = db.Column(db.String(50))
    find = db.Column(db.String(20))
    text = db.Column(db.String(200))

@app.route('/')
def landing():
   return render_template('landing.html')


@app.route('/thankyou', methods = ['POST'])
def thankyou():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    find = request.form['find-us']
    text = request.form['message']

    data = Users(name=name, phone=phone, email=email, text=text)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('landing'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
