# Sqlite in Python in Hindi | Python Tutorial For Beginners Series #16

import sqlite3

conn = sqlite3.connect('names.sql')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS friends(id REAL,name TEXT)")
def add_values():
    c.execute("INSERT INTO friends VALUES(1,'Ranuak'),(2,'Sumer')")
    conn.commit()
def retrive():
    c.execute('SELECT * FROM friends')
    views=c.fetchall()
    print(views)

create_table()
add_values()
retrive()