from flask import Flask,render_template,request,url_for,session,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,DateTimeField,RadioField,SelectField,TextAreaField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from controller.home import home

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acc_form')
def acc_form():
    return render_template('cr_acc.html')

@app.route('/requested_form')
def requested_form():
    return render_template('requested.html')

@app.route('/inc_share_form')
def inc_share_form():
    return render_template('inc_share.html')

@app.route('/withdraw_form')
def withdraw_form():
    return render_template('withdraw_share.html')

@app.route('/reciept_form')
def reciept_form():
    return render_template('reciept.html')

@app.route('/signin_form')
def signin_form():
    return render_template('signin.html')

@app.route('/acc_preview')
def acc_preview():
    return render_template('acc_preview.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)
