import os
import psycopg2
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

class Database:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._initialize_connection()
        return cls._instance

    def _initialize_connection(self):
        """Initialize the database connection"""
        try:
            self._connection = psycopg2.connect(
                dbname=os.getenv('DB_NAME'),
                host=os.getenv('DB_HOST'),  # Fix variable name
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),  # Fix variable name
                port=os.getenv('DB_PORT')
            )
            print("Database connection established.")
        except psycopg2.Error as e:
            print(f"Database connection error: {e}")
            self._connection = None

    def get_connection(self):
        """Return the existing database connection, or reinitialize if closed"""
        if self._connection is None or self._connection.closed:
            print("Re-establishing database connection...")
            self._initialize_connection()
        return self._connection

# Export instance
db_instance = Database()