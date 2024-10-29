from flask import Flask
from api import apiBp
from logic import myAPIbp
from authentication import authBp


app = Flask(__name__)
app.register_blueprint(apiBp)
app.register_blueprint(myAPIbp)
app.register_blueprint(authBp)


if __name__=='__main__':
    app.run(debug=True)