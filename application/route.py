from flask import Flask,redirect,url_for,render_template,request
from application import route
app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)