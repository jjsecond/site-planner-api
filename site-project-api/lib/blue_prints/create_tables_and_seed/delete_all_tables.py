from flask import jsonify
from lib.database.initialTableCreation import db_instance
import psycopg2.extras

def process_delete_all_tables():
    """Delete all tables and rows"""
    try:
        db = db_instance.get_connection()
        # This is used to return the result as a dictionary 
        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
    
            cur.execute('''
            DO $$ 
            DECLARE r RECORD;
            BEGIN 
            FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') 
            LOOP 
            EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
            END LOOP;
            END $$;
            ''') 

            db.commit()  # Commit the transaction
            print("All tables dropped successfully.")

            return 'All tables deleted and rows', 200
    except Exception as e:
        print("Error getting all sites: ", e)
        return jsonify({"error": "Internal Server Error"}), 500