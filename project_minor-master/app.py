from flask import Flask, render_template,session, redirect, request, flash
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from db import db1,db
import models
from models import Login

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

@app.route('/', methods = ['GET' , 'POST'])
def Contact():
    if request.method == 'POST':
        cname = request.form.get('c_name')
        cemail_id = request.form.get('c_email')
        cmessage = request.form.get('mssg')
        db.execute("""insert into contacts(name,email,message) VALUES('{}', '{}','{}')""".format(cname,cemail_id,cmessage))
        db.commit()
        print("mssg stored!")   
        return render_template('index.html')

    

    # if login==True:
    #     return render_template('home.html')
    # else:
    print("if condition is not executed btn")
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
        return redirect('/')

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
        
        return render_template('index.html')

    return render_template('login.html')

    # else:
    #     return render_template('login.html')

@app.route('/products', methods = ['GET','POST'])
def Store():
        data= db.execute('SELECT * FROM categories')
        # print(data.fetchall()[0][1])
       
        categories=data.fetchall()
       
        #[(1,name,data),(1,name,data),(1,name,data)]
        #   0 1   2      0  1   2
        #   0               1               2
        #fetchall[(),(),()]
        #fetchall()[0][1]
        
        
        return render_template('products.html',categories=categories)
  
@app.route('/cart', methods = ['GET','POST'])
def Cart():
    data = db.execute('SELECT * from categories')
    categories = data.fetchall()
    return render_template('cart.html',categories=categories)

@app.route('/admin', methods= ['GET','POST'])
def admin():
    if request.method == 'POST':
        p_id = request.form.get('p_id')
        p_name = request.form.get('p_name')
        p_type = request.form.get('p_type')
        p_image = request.form.get('p_image')
        p_desc = request.form.get('p_desc')
        p_quantity= request.form.get('p_quantity')
        p_amount = request.form.get('p_amount')
        email = request.form.get('email')
        contact = request.form.get('contact')
        db.execute("""INSERT INTO admin(p_id,p_name,p_type,p_image,p_desc,p_quantity,p_amount,email,contact) VALUES('{}', '{}', '{}', '{}','{}','{}','{}','{}','{}')""".format(p_id,p_name, p_type,p_image,p_desc,p_quantity,p_amount,email,contact))
        db.commit()
        return render_template('admin.html')
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug = True)
    db1.init_app(app)
