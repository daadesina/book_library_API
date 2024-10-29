from flask import Flask, request, render_template, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from form import LoginClass
from api import apiBp
from logic import myAPIbp
from authentication import authBp
from authentication import readAuthFunc



app = Flask(__name__)
app.config['SECRET_KEY'] = 'adesina'
app.register_blueprint(apiBp)
app.register_blueprint(myAPIbp)
app.register_blueprint(authBp)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = readAuthFunc()

@login_manager.user_loader
def load_user(user_id):
    for i in range(len(users)):
        if user_id in users[i]:
            return User(user_id)
    return None

@app.route('/login', methods = ['GET', 'POST'])
def login ():
    login_py = LoginClass()
    email_py = None
    password_py = None
    
    if request.method == 'POST':
        email_py = login_py.email.data
        password_py = login_py.password.data
        login_py.email.data = ""
        login_py.password.data = ""
        for i in range(len(users)):
            if users[i]['Email'] == email_py and users[i]['Password'] == password_py:
                email_py = User(email_py)
                login_user(email_py)
                return redirect(url_for('myAPI.home'))
        return 'Invalid Details'
    return render_template('login.html', login_html=login_py)




if __name__=='__main__':
    app.run(debug=True)