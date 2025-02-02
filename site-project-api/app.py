from flask import Flask, jsonify, request
# from flask_cors import CORS
from dotenv import load_dotenv
import os
# from lib.database.database import db_instance 
from lib.database.initialTableCreation import create_tables, seed_db,db_instance
from flask_cors import CORS
import psycopg2.extras

app = Flask(__name__)

# Blocking postman
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins


@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'


@app.route('/api/sites', methods=['GET'])
def getAll():
    """Get all sites"""
    try:
        db = db_instance.get_connection()
        # This is used to return the result as a dictionary 
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute('''SELECT * FROM site''') 

            data = cur.fetchall()

            if data is None:
                return False, 404

            data_as_dict = [dict(row) for row in data]

            return jsonify(data_as_dict), 200
    except Exception as e:
        print("Error getting all sites: ", e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/api/tasks', methods=['GET'])
def getTasks():
    """Get all tasks linked to a plot on a site"""
    try:
        plotId = request.args.get('plotId')

        db = db_instance.get_connection()
        # This is used to return the result as a dictionary 
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute('''
            SELECT s.id AS site_id, p.plot_number, t.task_name, t.task_type, t.trade, t.status, t.created_at AS task_created_at, t.updated_at AS task_update_at  
            FROM site AS s
            JOIN plot AS p ON s.id = p.site_id
            JOIN task AS t ON t.plot_id = p.id
            WHERE s.id = %(plotId)s
            ''', {'plotId': plotId})

            data = cur.fetchall()
            
            if data is None:
                return False, 404

            data_as_dict = [dict(row) for row in data]

            return jsonify(data_as_dict), 200
    except Exception as e:
        print("Error getting all tasks for a plot: ", e)
        return jsonify({"error": "Internal Server Error"}), 500


@app.route('/api/createAndSeed', methods=['GET'])
def createAllAndSeed():
    """Create all tables"""
    try:
        create_tables()
        seed_db()

        return 'successfully created all tables and seeded them'
    except Exception as e:
        print("Error creating tables or seeding db:", e)

if __name__ == '__main__':
    # debug mode will restart when we make changes
    app.run(debug=True)