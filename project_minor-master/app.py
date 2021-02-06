from flask import Flask, render_template,session, redirect, request
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from db import db1,db
import models
# import json

# with open('templates/config.json', 'r') as c:
    # params = json.load(c)["params"]

# local_server = True
# from models import Login

app = Flask(__name__)
app.secret_key = 'hello'
# if local_server:
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

@app.route('/', methods = ['GET' , 'POST'])
def Contact():
    if request.method == 'POST':
        cname = request.form.get('c_name')
        cemail_id = request.form.get('c_email')
        cmessage = request.form.get('mssg')
        db.execute("""insert into contacts(name,email,message) VALUES('{}', '{}','{}')""".format(cname,cemail_id,cmessage))
        db.commit()
        # print("mssg stored!")   
        return render_template('index.html')

    # print("if condition is not executed btn")
    return render_template('index.html')

@app.route('/signup', methods = ['GET','POST'])
def Signup():
    if request.method == 'POST':
        
        name = request.form.get('name')
        email_id = request.form.get('email_id')
        contact = request.form.get('contact')
        password = request.form.get('password')
        confirmpassword = request.form.get('confirmpassword')

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
        
        return render_template('products.html',categories=categories)
  
@app.route('/cart', methods = ['GET','POST'])
def Cart():
    data = db.execute('SELECT * from categories')
    categories = data.fetchall()
    return render_template('cart.html',categories=categories)

@app.route('/adminlog', methods=['GET','POST'])
def adminlog():
    # if ('user' in session and session['user'] == params['admin_user']):
    #     return render_template('admin.html', params=params)
    # if request.method == 'POST':
    #     session.pop(username,None)

    if request.method == 'POST':
        request.form['password'] == 'password'
        session['username'] == request.form['username']
        return redirect(url_for('admin.html'))

    return render_template('adminlog.html')




    # if request.method == 'POST':
    #     username = request.form.get('uname')
    #     userpass = request.form.get('pass')
    #     if (username == params['admin_user'] and userpass == params["admin_password"]):
    #         session['user'] = username
    #         # return "logged in"
    #         return render_template('admin.html', params=params)
            
    # return render_template('adminlog.html', params = params)



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/adminlog')

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
        # db.execute("""INSERT INTO categories(p_id,p_name,p_type,p_image,p_desc,p_quantity,p_amount) VALUES('{}', '{}', '{}', '{}','{}','{}','{}')""".format(p_id,p_name, p_type,p_image,p_desc,p_quantity,p_amount))
        # db.commit()
        return render_template('admin.html')
    return render_template('admin.html')

@app.route('/Prod_del' ,methods=['GET','POST'])
def delete():
    data = db.execute('SELECT * from categories')
    categories = data.fetchall()
    return render_template('Product_del.html',categories=categories)



@app.route('/delete/<int:pid>' ,methods=['GET','POST'])
def dele(pid):
    global categories
    i = 0
    deleted = False

    for products in categories:
        if products['id'] == id:
            categories.pop(i)
            deleted = True

        i += 1

    if deleted:
        return redirect('Product_del.html')

    return redirect('Product_del.html')

    




    # post = Categories.query.fetchall(p_id=pid).first()
    # db.session.delete(post)
    # db.session.commit()    
    # return "DELETED"

   
    

        # dlt =  Categories.query.filter_by().all()
        
        # return render_template('Product_del.html',row = dlt)

        # prdct = request.form      
        # pd = prdct['p_id']
        # db.execute("delete from categories where p_id='"+p_id+"'") 
        # db.commit()  
        # admin = session.query(Admin).filter(Admin.p_name=='abx').first()
        # session.delete(admin)
        # session.commit()
        
    #     if p_id in admin:
    #         db.execute("DELETE FROM admin WHERE p_id = 100 ")
    #         db.commit() 
    #     else:
    #         print('Incorrect Product ID')
    #     return render_template('Product_del.html')    
    # return render_template('Product_del.html')



if __name__ == '__main__':
    # db.init_app(app)
    app.run(debug = True)
    db.init_app(app)