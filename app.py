from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def land():
    return render_template('index.html')
@app.route('/login')
def login():
    if session.get('logged_in'):
        return render_template('home.html')
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/home', methods=['POST'])
def home():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return login()

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return land()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
