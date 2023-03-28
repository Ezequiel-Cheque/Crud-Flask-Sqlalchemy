from flask import Flask
from routes.contacts import contacts
from utils.db import db
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

app.secret_key = "development"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(contacts)