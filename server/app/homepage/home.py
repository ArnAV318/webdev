from flask import Flask,render_template, Blueprint
home = Blueprint('homepage',__name__)

@home.route('/home')
def homepage():
    return render_template('home.html')


