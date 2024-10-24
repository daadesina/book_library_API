from flask import Flask, request, Blueprint
import json, sqlite3
from functionsAPI import connectDB, readFunc, writeFunc, readSpecFunc, updateSpecFunc, deleteSpecFunc

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
       return(readFunc())
        
    if request.method == "POST":
        my_title = request.form["Title"]
        my_author = request.form["Author"]
        my_subject = request.form["Subject"]
        my_link = request.form["Link"]
        
        myData = writeFunc(my_title, my_author, my_subject, my_link)
        
        return(myData)
    
@apiBp.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE' ])
def single_book(id):
    if request.method == 'GET':
        return(readSpecFunc(id))
    
    if request.method == "PUT":
        my_title = request.form["Title"]
        my_author = request.form["Author"]
        my_subject = request.form["Subject"]
        my_link = request.form["Link"]
        
        myData = updateSpecFunc(my_title, my_author, my_subject, my_link, id)
        
        return(myData)
    
    if request.method == "DELETE":
        return(deleteSpecFunc(id))