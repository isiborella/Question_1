from flask import Flask,redirect,url_for,render_template,request
from application import app
app=Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

#from .routes import *
from application import route