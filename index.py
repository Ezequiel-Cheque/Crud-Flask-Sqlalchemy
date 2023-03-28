from app import app
from utils.db import db

import config

@app.before_request
def init_bd():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)