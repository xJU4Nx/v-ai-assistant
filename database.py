import sqlite3

DATABASE = "assistant.db"


def create_database():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            due_date TEXT,
            status TEXT DEFAULT 'Not Started'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            date_applied TEXT,
            status TEXT DEFAULT 'Applied',
            follow_up_date TEXT
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()