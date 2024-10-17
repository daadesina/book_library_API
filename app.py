from flask import Flask, request
import json, sqlite3

app = Flask(__name__)

def connectDB():
    try:
        conn = sqlite3.connect("books.sqlite")
    except Exception as myError:
        print(myError)
    return conn

myDatabase = connectDB()
myDatabase.execute("""CREATE TABLE IF NOT EXISTS books(
    id integer PRIMARY KEY,
    Author text NOT NULL,
    Country text NOT NULL,
    Title text NOT NULL,
    Year text NOT NULL
    )""")

def readFunc():
    myDatabase = connectDB()
    allBook = myDatabase.execute("""SELECT * FROM books""")
    allBookData = allBook.fetchall()
    allBookArray = []
    for i in range(len(allBookData)):
        for num in allBookData[i]:
            myBook = dict(id=allBookData[i][0], Author=allBookData[i][1], Country=allBookData[i][2], Title=allBookData[i][3], Year= allBookData[i][4])
        allBookArray = allBookArray + [myBook]
    return (json.dumps(allBookArray))

def writeFunc(Author, Country, Title, Year):
    myDatabase = connectDB()
    myWrite = """INSERT INTO books(Author, Country, Title, Year)
                VALUES(?, ?, ?, ?)
    """
    myDatabase.execute(myWrite, (Author, Country, Title, Year))
    myDatabase.commit()
    return(readFunc())
            
@app.route('/books', methods = ["GET", "POST"])
def books ():
    if request.method == "GET":
       return(readFunc())
        
    if request.method == "POST":
        my_author = request.form["Author"]
        my_country = request.form["Country"]
        my_title = request.form["Title"]
        my_year = request.form["Year"]
        
        myData = writeFunc(my_author, my_country, my_title, my_year)
        
        return(myData)
    
@app.route('/books/<int:id>', methods = ['GET', 'PUT', 'DELETE' ])
def single_book(id):
    def myGet(id):
        myDatabase = connectDB()
        allBook = myDatabase.execute("""SELECT * FROM  books""")
        allBookData = allBook.fetchall()
        specBook = allBookData[id-1]
        for num in range(len(specBook)):
            myBook = dict(id=specBook[0], Author=specBook[1], Country=specBook[2], Title=specBook[3], Year=specBook[4])
        return(json.dumps(myBook))
     
    def upDate(Author, Country, Title, Year, id):
        myDatabase = connectDB()
        myBook = """UPDATE books SET 
                    Author = ?,
                    Country = ?,
                    Title = ?,
                    Year = ?
                    WHERE id = ?
                    """
        myDatabase.execute(myBook, (Author, Country, Title, Year, id))
        myDatabase.commit()
        return(readFunc())
    
    def deleteFunc(id):
        myDatabase = connectDB()
        myDelete = """DELETE FROM books WHERE id = ?"""
        myDatabase.execute(myDelete, (id,))
        myDatabase.commit()
        return(readFunc())
         
    if request.method == 'GET':
        return(myGet(id))
    
    if request.method == "PUT":
        my_author = request.form["Author"]
        my_country = request.form["Country"]
        my_title = request.form["Title"]
        my_year = request.form["Year"]
        
        myData = upDate(my_author, my_country, my_title, my_year, id)
        
        return(myData)
    
    if request.method == "DELETE":
        return(deleteFunc(id))
  
if __name__ == '__main__':
    app.run(debug=True)