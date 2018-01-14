from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
Bootstrap(app)


from views import *

if __name__ == '__main__':
    db.create_all()
    print("starting application....")
    app.run(debug=True)




