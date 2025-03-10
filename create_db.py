import sqlite3

DATABASE = 'symptoms.db'

def init():
    print("Se creează baza de date...")
    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS symptoms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symptom TEXT NOT NULL
            )
        """)
        connection.commit()
    print("Baza de date a fost creată.")

# Call the init function when the script is run
if __name__ == '__main__':
    init()
