from lib.database.database import db_instance 
import os

SQL_FOLDER_TABLES = "lib/database/createTables"
SQL_FOLDER_DUMMY_DATA = "lib/database/dummyData"

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

        sql_table_files = sorted(f for f in os.listdir(SQL_FOLDER_TABLES) if f.endswith(".sql"))

        for sql_table_file in sql_table_files:
            file_path = os.path.join(SQL_FOLDER_TABLES, sql_table_file)
            execute_sql_file(cur, file_path)

        db.commit()
        cur.close()
        print("All tables and enums created successfully!")
    except Exception as e:
        print("Error creating tables or enums:", e)

def seed_db():
    try:
        db = db_instance.get_connection()
        cur = db.cursor()

        print("Got to here")

        sql_dummy_data_files = sorted(f for f in os.listdir(SQL_FOLDER_DUMMY_DATA) if f.endswith(".sql"))

        for sql_data_file in sql_dummy_data_files:
            file_path = os.path.join(SQL_FOLDER_DUMMY_DATA, sql_data_file)
            execute_sql_file(cur, file_path)

        db.commit()
        cur.close()
        print("All rows to all tables added successfully!")

    except Exception as e:
        print("Error adding rows to tables:", e)
