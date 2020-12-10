from flask import Flask, render_template,session, redirect, request
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
engine = create_engine('mysql+mysqlconnector://root:@localhost/neev')
app.config['SQLAlchemy_DATABASE_URI'] = 'mysql+mysqlconnector://root:localhost/neev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db1=SQLAlchemy() # For Database creation
db = scoped_session(sessionmaker(bind=engine)) #For DB commits Insert,Delete,select,(queries)