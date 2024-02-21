import sqlite3

# Function to create a SQLite database connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('harmony.db')
        print("Database connection established successfully")
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
    return conn

# Function to create the users table in the database
def create_users_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        print("Users table created successfully")
    except sqlite3.Error as e:
        print("Error creating users table:", e)

# Function to create the songs table in the database
def create_songs_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                genre TEXT
            )
        """)
        print("Songs table created successfully")
    except sqlite3.Error as e:
        print("Error creating songs table:", e)

# Main function to create the database schema
def create_schema():
    conn = create_connection()
    if conn is not None:
        create_users_table(conn)
        create_songs_table(conn)
        conn.close()
    else:
        print("Error: Unable to establish database connection")

if __name__ == "__main__":
    create_schema()
