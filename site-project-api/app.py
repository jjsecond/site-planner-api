from flask import Flask
# from flask_cors import CORS
from dotenv import load_dotenv
import os
# from lib.database.database import db_instance 
from lib.database.initialTableCreation import create_tables, seed_db

app = Flask(__name__)


load_dotenv()

init_db = os.getenv('LOAD_INIT_SCRIPT')

if(init_db == "True"):
    # Add check to ensure tables have been created so whether to seed or not and create tables
    create_tables()
    seed_db()


@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    # debug mode will restart when we make changes
    app.run(debug=True)