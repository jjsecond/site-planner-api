from flask import jsonify
from lib.database.initialTableCreation import db_instance
import psycopg2.extras

def process_get_all_sites():
    """Get all sites"""
    try:
        db = db_instance.get_connection()
        # This is used to return the result as a dictionary 
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute('''SELECT * FROM sites''') 

            data = cur.fetchall()

            if data is None:
                return False, 404

            data_as_dict = [dict(row) for row in data]

            return jsonify(data_as_dict), 200
    except Exception as e:
        print("Error getting all sites: ", e)
        return jsonify({"error": "Internal Server Error"}), 500