from flask import Flask, render_template,session, redirect, request, flash
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from db import db1,db
from models import Login

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def home():
    # if login==True:
    #     return render_template('home.html')
    # else:
        return render_template('index.html')

@app.route('/signup', methods = ['GET','POST'])
def Signup():
    if request.method == 'POST':
        
        name = request.form.get('name')
        email_id = request.form.get('email_id')
        contact = request.form.get('contact')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')

        # if Name == '' or Email == '' or Contact == '' or Password == '' or ConfirmPass == '':
            # print('Wrong entries')

        db.execute("""INSERT INTO signup(id,name,email_id,contact,password,confirmpassword) VALUES(NULL,'{}', '{}','{}','{}','{}')""".format(name,email_id,contact,password,confirmpassword))
        # db.execute('INSERT INTO signup(Name,Email,Contact,Password,ConfirmPass) VALUES(:Name, :Email, :Contact, :Password, :ConfirmPass)',{'Name':Name,'Email':Email,'Contact':Contact,'Password':Password,'ConfirmPass':ConfirmPass})
        db.commit()
        return render_template('index.html')

    return render_template('signup.html')  
  

@app.route('/login', methods = ['GET', 'POST'])
def UserLogin():
    
    if request.method == 'POST':
        username= request.form.get('username')
        password = request.form.get('password')
        session['username'] = username
        session['password'] = password
        db.execute('INSERT INTO login(username,password) VALUES(:username,:password)',{'username':username,'password':password})
        db.commit()
        # userInfo = Login.query.filter_by(username=username).first()
        # context={
        #     "info":userInfo
        # }
        # return render_template('index.html')
        return redirect('/')

    return render_template('login.html')

    # else:
    #     return render_template('login.html')

@app.route('/products', methods = ['GET','POST'])
def Store():
     return render_template('products.html')
  
    
if __name__ == '__main__':
    app.run(debug = True)
