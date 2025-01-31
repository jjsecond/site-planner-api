from lib.database.database import db_instance 
import os

SQL_FOLDER = "lib/database/createTables"

def execute_sql_file(cursor, file_path):
    """ Reads and executes an SQL file. """
    with open(file_path, "r") as sql_file:
        sql_script = sql_file.read()
        cursor.execute(sql_script)
        print(f"Executed {file_path}")

def create_tables():
    try:
        db = db_instance.get_connection()
        cur = db.cursor()

        sql_files = sorted(f for f in os.listdir(SQL_FOLDER) if f.endswith(".sql"))

        for sql_file in sql_files:
            file_path = os.path.join(SQL_FOLDER, sql_file)
            execute_sql_file(cur, file_path)

        db.commit()
        cur.close()
        db.close()
        print("All tables and enums created successfully!")
    except Exception as e:
        print("Error creating tables or enums", e)
