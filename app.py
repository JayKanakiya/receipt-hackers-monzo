from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import mysql.connector


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def land():
    return render_template('index.html')

@app.route('/verifyDetails',methods=['GET','POST'])
def SQLData():
    name = request.form['name']
    email = request.form['email']
    uname = request.form['username']
    passwd = request.form['password']
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="jaymk",
      database="receipt_login"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO user (name, email, uname, pass) VALUES (%s, %s, %s, %s)"
    val = (name,email, uname, passwd)
    mycursor.execute(sql,val)
    mydb.commit()
    return login()

@app.route('/login')
def login():
    if session.get('logged_in'):
        return render_template('home.html')
    return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
    return render_template('signup.html')

@app.route('/home', methods=['POST'])
def home():
    username = request.form['username']
    passwd = request.form['password']
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="jaymk",
      database="receipt_login"
    )

    mycursor = mydb.cursor()
    sql1= "SELECT uname,name from user where pass = %s"
    val=(passwd, )
    mycursor.execute(sql1,val)

    myresult = mycursor.fetchone()
    if myresult==None:
        return login()
    if myresult!=None:
        print(myresult)
        session['name'] = myresult[1]
        if myresult[0]==username:
            session['logged_in'] = True
            return render_template('home.html')
        # if request.form['password'] == 'password' and request.form['username'] == 'admin':
        #     session['logged_in'] = True
    else:
        flash('wrong password!')
    return login()

def redirectHome():
    if session['logged_in'] == True:
        return render_template('home.html')



@app.route('/logout')
def logout():
    session['logged_in'] = False
    return land()

@app.route('/upload',methods=['POST'])
def upload():
    session['logged_in'] = True
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        filename = file.filename
        dest = '/'.join([target,'1.jpg'])
        file.save(dest)
        break

    return redirectHome()

@app.route('/view')
def view():
    return render_template('view.htmlS')

@app.route('/file')
def file():
    return render_template('upload.html')
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=0000)
