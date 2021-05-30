from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SECRET_KEY'] = "ytiyfkugkudkydd"
app.secret_key = 'agieigepg'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/product.db'
db = SQLAlchemy(app)
import catalouge.routes