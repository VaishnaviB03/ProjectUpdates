from flask import Flask, render_template,session, redirect, request
from sqlalchemy import create_engine 
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from db import db1,db

app = Flask(__name__)

class Login(db1.Model): 
    id = db1.Column(db1.Integer, primary_key = True)
    username = db1.Column(db1.String(20), unique = True, nullable = False)
    password = db1.Column(db1.String(10), unique = True, nullable = False)

class Signup(db1.Model):
    id = db1.Column(db1.Integer, primary_key = True)
    name = db1.Column(db1.String(20),unique = True)
    email_id = db1.Column(db1.String(30),unique = True)
    contact = db1.Column(db1.Integer,unique = True)
    password = db1.Column(db1.String(20),unique = True)
    confirmpassword = db1.Column(db1.String(20),unique = True)

class Contacts(db1.Model):
    id = db1.Column(db1.Integer, primary_key = True)
    name =  db1.Column(db1.String(20),unique = True)
    email =  db1.Column(db1.String(20),unique = True)
    message =  db1.Column(db1.String(200),unique = True)
