from lib.database.initialTableCreation import create_tables, seed_db

def process_create_tables_and_seed():
    """Create all tables"""
    try:
        create_tables()
        seed_db()

        return 'successfully created all tables and seeded them', 200
    except Exception as e:
        print("Error creating tables or seeding db:", e)
        return 'Internal Server Error', 500