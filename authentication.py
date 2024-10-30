from flask import Blueprint, render_template, url_for, request, redirect
from form import SignupClass, LoginClass
import json, sqlite3

authBp = Blueprint('authentication', __name__)


def connectAuthDB():
    try:
        conn = sqlite3.connect("auth.sqlite")
    except Exception as myError:
        print(myError)
    return conn

myAuthDatabase = connectAuthDB()
myAuthDatabase.execute("""CREATE TABLE IF NOT EXISTS auth(
    id integer PRIMARY KEY,
    First_Name text NOT NULL,
    Last_Name text NOT NULL,
    Email text NOT NULL,
    Password text NOT NULL
    )""")
myAuthDatabase.commit


def readAuthFunc():
    myAuthDatabase = connectAuthDB()
    myAuthDatabase.commit()
    allAuth = myAuthDatabase.execute("""SELECT * FROM auth""")
    allAuthData = allAuth.fetchall()
    allAuthArray = []
    for i in range(len(allAuthData)):
        for num in allAuthData[i]:
            myAuth = dict(id=allAuthData[i][0], First_Name=allAuthData[i][1], Last_Name=allAuthData[i][2], Email=allAuthData[i][3], Password= allAuthData[i][4])
        allAuthArray = allAuthArray + [myAuth]
    # return (json.dumps(allAuthArray))
    return(allAuthArray)


def writeAuthFunc(First_Name, Last_Name, Email, Password):
    myAuthDatabase = connectAuthDB()
    myAuthWrite = """INSERT INTO auth(First_Name, Last_Name, Email, Password)
                VALUES(?, ?, ?, ?)
    """
    myAuthDatabase.execute(myAuthWrite, (First_Name, Last_Name, Email, Password))
    myAuthDatabase.commit()
    return(readAuthFunc())

def readAuthSpecFunc(id):
        myAuthDatabase = connectAuthDB()
        allAuth = myAuthDatabase.execute("""SELECT * FROM  auth""")
        allAuthData = allAuth.fetchall()
        specAuth = allAuthData[id-1]
        for num in range(len(specAuth)):
            myAuth = dict(id=specAuth[0], First_Name=specAuth[1], Last_Name=specAuth[2], Email=specAuth[3], Password=specAuth[4])
        return(myAuth)
     
def updateAuthSpecFunc(First_Name, Last_Name, Email, Password, id):
        myAuthDatabase = connectAuthDB()
        myAuth = """UPDATE auth SET 
                    First_Name = ?,
                    Last_Name = ?,
                    Email = ?,
                    Password = ?
                    WHERE id = ?
                    """
        myAuthDatabase.execute(myAuth, (First_Name, Last_Name, Email, Password, id))
        myAuthDatabase.commit()
        return(readAuthFunc())
    
def deleteAuthSpecFunc(id):
        myAuthDatabase = connectAuthDB()
        myAuthDelete = """DELETE FROM auth WHERE id = ?"""
        myAuthDatabase.execute(myAuthDelete, (id,))
        myAuthDatabase.commit()
        return(readAuthFunc())




@authBp.route('/')
def landingPage():
    return render_template('/landing_page.html')

@authBp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name_py = request.form['first_name_html']
        last_name_py = request.form['last_name_html']
        email_py = request.form['email_html']
        password_py = request.form['password_html']
        readAuth = readAuthFunc()
        for i in range(len(readAuth)):
            if readAuth[i]['Email'] == email_py:
                return ('Email Taken')
        writeAuthFunc(first_name_py, last_name_py, email_py, password_py)
        return redirect(url_for("login"))
    return render_template('signup.html')

