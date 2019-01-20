from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from main import ReceiptsClient
import config
import json
import mysql.connector

# at the beginning of starting the app, authorize it
client = ReceiptsClient()
client.do_auth()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

    return connect_monzo()

@app.route('/view')
def view():
    return render_template('view.htmlS')

@app.route('/file')
def file():
    return render_template('upload.html')

@app.route('/monzo')
def connect_monzo(x1=None):
    if x1 is None:
        x1 = json.dumps({
                      "transaction_id": "tx_00009ezCURJniYB2dnnopt",
                      "external_id": "test-receipt-3",
                      "total": 1,
                      "currency": "GBP",
                      "items": [
                        {
                          "description": "Apples, 20p per kg",
                          "quantity": 18.56,
                          "unit": "kg",
                          "amount": 700,
                          "currency": "GBP"
                        }
                      ]
                        }
                        )
    # client = ReceiptsClient()
    # client.do_auth()
    client._api_client.api_put("transaction-receipts/", x1)
    flash('Uploaded to Monzo!')
    return redirectHome()
    # return "Check Monzo - uploaded"

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=0000)
