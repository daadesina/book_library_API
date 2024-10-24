import json, sqlite3

def connectDB():
    try:
        conn = sqlite3.connect("books.sqlite")
    except Exception as myError:
        print(myError)
    return conn

def readFunc():
    myDatabase = connectDB()
    myDatabase.commit()
    allBook = myDatabase.execute("""SELECT * FROM books""")
    allBookData = allBook.fetchall()
    allBookArray = []
    for i in range(len(allBookData)):
        for num in allBookData[i]:
            myBook = dict(id=allBookData[i][0], Title=allBookData[i][1], Author=allBookData[i][2], Subject=allBookData[i][3], Link= allBookData[i][4])
        allBookArray = allBookArray + [myBook]
    return (json.dumps(allBookArray))

def writeFunc(Title, Author, Subject, Link):
    myDatabase = connectDB()
    myWrite = """INSERT INTO books(Title, Author, Subject, Link)
                VALUES(?, ?, ?, ?)
    """
    myDatabase.execute(myWrite, (Title, Author, Subject, Link))
    myDatabase.commit()
    return(readFunc())


def allBooksFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        arra = arra + [allBooks[i]]
    return (arra)


def programmingFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "Programming":
            arra = arra + [allBooks[i]]
    return (arra)

def africaFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "Africa":
            arra = arra + [allBooks[i]]
    return (arra)

def philosophyFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "Philosophy":
            arra = arra + [allBooks[i]]
    return (arra)

def novelFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "Novel":
            arra = arra + [allBooks[i]]
    return (arra)

def historyFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "History":
            arra = arra + [allBooks[i]]
    return (arra)

def economicsFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == "Economics":
            arra = arra + [allBooks[i]]
    return (arra)

def authorSearchFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
            arra = arra + [allBooks[i]['Author']]

    mySet = list(set(arra))
    return(sorted(mySet))

def subjectSearchFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
            arra = arra + [allBooks[i]['Subject']]

    mySet = list(set(arra))
    return(sorted(mySet))

def titleSearchFunc():
    allBooks = json.loads(readFunc())
    arra = []
    for i in range(len(allBooks)):
            arra = arra + [allBooks[i]['Title']]

    mySet = list(set(arra))
    return(sorted(mySet))


def searchByAuthorFunc(author):
    allBooks = json.loads(readFunc())
    arr = []
    element = []
    for i in range(len(allBooks)):
        if allBooks[i]['Author'] == author:
            arr = arr + [allBooks[i]]
    return (arr)

def searchBySubjectFunc(subject):
    allBooks = json.loads(readFunc())
    arr = []
    element = []
    for i in range(len(allBooks)):
        if allBooks[i]['Subject'] == subject:
            arr = arr + [allBooks[i]]
    return (arr)

def searchByTitleFunc(title):
    allBooks = json.loads(readFunc())
    arr = []
    element = []
    for i in range(len(allBooks)):
        if allBooks[i]['Title'] == title:
            arr = arr + [allBooks[i]]
    return (arr)


def readSpecFunc(id):
        myDatabase = connectDB()
        allBook = myDatabase.execute("""SELECT * FROM  books""")
        allBookData = allBook.fetchall()
        specBook = allBookData[id-1]
        for num in range(len(specBook)):
            myBook = dict(id=specBook[0], Title=specBook[1], Author=specBook[2], Subject=specBook[3], Link=specBook[4])
        return(json.dumps(myBook))
     
def updateSpecFunc(Title, Author, Subject, Link, id):
        myDatabase = connectDB()
        myBook = """UPDATE books SET 
                    Title = ?,
                    Author = ?,
                    Subject = ?,
                    Link = ?
                    WHERE id = ?
                    """
        myDatabase.execute(myBook, (Title, Author, Subject, Link, id))
        myDatabase.commit()
        return(readFunc())
    
def deleteSpecFunc(id):
        myDatabase = connectDB()
        myDelete = """DELETE FROM books WHERE id = ?"""
        myDatabase.execute(myDelete, (id,))
        myDatabase.commit()
        return(readFunc())

