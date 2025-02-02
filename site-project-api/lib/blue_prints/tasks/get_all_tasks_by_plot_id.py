from flask import jsonify, request
from lib.database.initialTableCreation import db_instance
import psycopg2.extras


def process_get_all_tasks_by_plot_id():
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