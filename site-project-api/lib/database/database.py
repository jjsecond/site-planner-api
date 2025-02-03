import os
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()

# JJ FYI: This can be switched to multithreading. By default flask uses Werkzeug(a Web Server Gateway Interface WSGI)
# can switch to multi threads and make the app multithreaded.
conn_pool = pool.SimpleConnectionPool(
    minconn=2,
    maxconn=20,
    dbname=os.getenv('DB_NAME'),
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    port=os.getenv('DB_PORT')
)

def get_connection():
    """Get a connection to DB"""
    return conn_pool.getconn()

def release_connection(conn):
    """Return connection to the pool after request is handled."""
    conn_pool.putconn(conn)
