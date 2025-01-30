from flask import Flask
from flask_cors import CORS
import psycopg2
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Access environment variables
dbName = os.getenv('DB_NAME')
dbhHost = os.getenv('B_HOST')
dbPassword = os.getenv('DB_PASSWORDY')
dbUser = os.getenv('DB_USER')
dbPort = os.getenv('DB_PORT')

conn = psycopg2.connect(dbname=dbName,
                        host=dbhHost,
                        user=dbUser,
                        password=dbPassword,
                        port=dbPort)


# Used to execute commands
cur = conn.cursor()

conn.commit()

print("here")
cur.execute("""CREATE TABLE IF NOT EXISTS person(
            id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            age INT,
            gender VARCHAR(25)
            );     
""")

    # Insert a test record (optional)
cur.execute("INSERT INTO person (name, age, gender) VALUES (%s, %s, %s) RETURNING id;", ('John Doe', 30, 'Male'))
new_id = cur.fetchone()[0]
conn.commit()
print(f"Inserted test record with ID: {new_id}")

    # Fetch all records to verify connection
cur.execute("SELECT * FROM person;")
rows = cur.fetchall()
print("Existing records:", rows)

cur.close()
conn.close()

@app.route('/')
def home():
    return '<h1>Flask REST API</h1>'

if __name__ == '__main__':
    # debug mode will restart when we make changes
    app.run(debug=True)