import sqlite3
import os
print("Current working directory:", os.getcwd())
print("Expected database path:", os.path.abspath("contacts.db"))
con = sqlite3.connect('contacts.db')
cur = con.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    email TEXT,
    phone int
)
''')
con.commit()
con.close()
print("contacts.db created successfully!")