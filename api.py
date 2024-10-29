from flask import Flask, request, Blueprint, jsonify
import json, sqlite3
from functionsAPI import connectDB, readFunc, writeFunc, readSpecFunc, updateSpecFunc, deleteSpecFunc
from authentication import connectAuthDB, readAuthFunc, readAuthSpecFunc, updateAuthSpecFunc, deleteAuthSpecFunc, writeAuthFunc

apiBp = Blueprint("apiBp", __name__)


myDatabase = connectDB()
myDatabase.execute("""CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    Title text NOT NULL,
    Author text NOT NULL,
    Subject text NOT NULL,
    Link text NOT NULL
    )""")
myDatabase.commit

            
@apiBp.route('/books', methods = ["GET", "POST"])
def books ():
    if request.method == "GET":
       return jsonify(readFunc())
        
    if request.method == "POST":
        my_title = request.form["Title"]
        my_author = request.form["Author"]
        my_subject = request.form["Subject"]
        my_link = request.form["Link"]
        
        myData = writeFunc(my_title, my_author, my_subject, my_link)
        
        return jsonify(myData)
    
@apiBp.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE' ])
def single_book(id):
    if request.method == 'GET':
        return jsonify(readSpecFunc(id))
    
    if request.method == "PUT":
        my_title = request.form["Title"]
        my_author = request.form["Author"]
        my_subject = request.form["Subject"]
        my_link = request.form["Link"]
        
        myData = updateSpecFunc(my_title, my_author, my_subject, my_link, id)
        
        return jsonify(myData)
    
    if request.method == "DELETE":
        return jsonify(deleteSpecFunc(id))
    





@apiBp.route('/auth', methods = ["GET", "POST"])
def account ():
    if request.method == "GET":
       return jsonify(readAuthFunc())
        
    if request.method == "POST":
        first_name = request.form["First_Name"]
        last_name = request.form["Last_Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        
        myData = writeAuthFunc(first_name, last_name, email, password)
        
        return jsonify(myData)
    
@apiBp.route('/auth/<int:id>', methods = ['GET', 'PUT', 'DELETE' ])
def single_account(id):
    if request.method == 'GET':
        return jsonify(readAuthSpecFunc(id))
    
    if request.method == "PUT":
        first_name = request.form["First_Name"]
        last_name = request.form["Last_Name"]
        email = request.form["Email"]
        password = request.form["Password"]
        
        myData = updateAuthSpecFunc(first_name, last_name, email, password, id)
        
        return jsonify(myData)
    
    if request.method == "DELETE":
        return jsonify(deleteAuthSpecFunc(id))