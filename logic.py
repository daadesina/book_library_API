from flask import request, Blueprint, render_template, redirect, url_for
import json, sqlite3
from functionsAPI import connectDB, readFunc, writeFunc, readSpecFunc, updateSpecFunc, deleteSpecFunc, authorSearchFunc
from functionsAPI import subjectSearchFunc, titleSearchFunc, searchByAuthorFunc, searchBySubjectFunc, searchByTitleFunc
from functionsAPI import programmingFunc, africaFunc, philosophyFunc, novelFunc, historyFunc, economicsFunc, allBooksFunc, deleteSpecFunc


myAPIbp = Blueprint("myAPI", __name__)


            
@myAPIbp.route('/', methods = ["GET", "POST"])
def home ():
    if request.method == "GET":
        (readFunc())
        return render_template('home.html')
    
    if request.method == "POST":
        allBooks = json.loads(readFunc())
        author_search = authorSearchFunc()
        subject_search = subjectSearchFunc()
        title_search = titleSearchFunc()
        search_by_py = request.form['search_by_html']
        if search_by_py == 'Search by Author':
            return render_template('search_author.html', myBooks=author_search, len_allBooks=len(author_search))
        elif search_by_py == 'Search by Subject':
            return render_template('search_subject.html', myBooks=subject_search, len_allBooks=len(subject_search))
        elif search_by_py == 'Search by Title':
            return render_template('search_title.html', myBooks=title_search, len_allBooks=len(title_search))
        else:
            return render_template('home.html')
    
@myAPIbp.route('/search_by_author', methods=['GET', 'POST'])
def search_by_author():
    if request.method == 'GET':
        return render_template('search_by_author.html')
    if request.method == 'POST':
        author_py = request.form['search_Author']
        searchByAuthor = searchByAuthorFunc(author_py)
        readFunc()
        return render_template('search_by_author.html', element=searchByAuthor, len_element=len(searchByAuthor))

@myAPIbp.route('/search_by_subject', methods=['GET', 'POST'])
def search_by_subject():
    if request.method == 'GET':
        return render_template('search_by_subject.html')
    if request.method == 'POST':
        subject_py = request.form['search_Subject']
        searchBySubject = searchBySubjectFunc(subject_py)
        return render_template('search_by_subject.html', element=searchBySubject, len_element=len(searchBySubject))

@myAPIbp.route('/search_by_title', methods=['GET', 'POST'])
def search_by_title():
    if request.method == 'GET':
        return render_template('search_by_title.html')
    if request.method == 'POST':
        title_py = request.form['search_Title']
        searchByTitle = searchByTitleFunc(title_py)
        return render_template('search_by_title.html', element=searchByTitle, len_element=len(searchByTitle))
    


@myAPIbp.route('/programming', methods=['GET', 'POST'])
def programming():
        program = programmingFunc()
        return render_template('programming.html', element=program, len_element=len(program))

@myAPIbp.route('/africa', methods=['GET', 'POST'])
def africa():
        program = africaFunc()
        return render_template('africa.html', element=program, len_element=len(program))

@myAPIbp.route('/philosophy', methods=['GET', 'POST'])
def philosophy():
        program = philosophyFunc()
        return render_template('philosophy.html', element=program, len_element=len(program))

@myAPIbp.route('/novel', methods=['GET', 'POST'])
def novel():
        program = novelFunc()
        return render_template('novel.html', element=program, len_element=len(program))

@myAPIbp.route('/history', methods=['GET', 'POST'])
def history():
        program = historyFunc()
        return render_template('history.html', element=program, len_element=len(program))

@myAPIbp.route('/economics', methods=['GET', 'POST'])
def econimics():
        program = economicsFunc()
        return render_template('economics.html', element=program, len_element=len(program))


@myAPIbp.route('/all_books', methods=['GET', 'POST'])
def allBooksDef():
        program = allBooksFunc()
        return render_template('allBooks.html', element=program, len_element=len(program))



@myAPIbp.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('/upload.html')
    if request.method == 'POST':
        Title_py = request.form['Title_html']
        Author_py = request.form['Author_html']
        Subject_py = request.form['Subject_html']
        Link_py = request.form['Link_html']
        myData = writeFunc(Title_py, Author_py, Subject_py, Link_py)
        # return redirect(url_for('myAPI.home'))
        return render_template('home.html')
    




@myAPIbp.route('/get_data')
def get_data():
    return(readFunc())
    
@myAPIbp.route('/api/data/<int:id>', methods = ['GET', 'PUT', 'DELETE' ])
def single_book(id):
    
    if request.method == 'GET':
        return(readSpecFunc(id))
    
    if request.method == "PUT":
        my_author = request.form["Author"]
        my_country = request.form["Country"]
        my_title = request.form["Title"]
        my_year = request.form["Year"]
        
        myData = updateSpecFunc(my_author, my_country, my_title, my_year, id)
        
        return(myData)
    
    if request.method == "DELETE":
        return(deleteSpecFunc(id))