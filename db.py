import sqlite3


def connect_to_db():
    return sqlite3.connect("hexcodes.db")

def select_column(conn) -> tuple:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS hexcodes (id int PRIMARY KEY, hexcode_hash char(65) NOT NULL)")
    c.execute("SELECT hexcode_hash FROM hexcodes")
    results = c.fetchall()
    return results, c

def drop_table(conn, c):
    c.execute("DROP TABLE hexcodes")
    conn.commit()
    
def insert_into_db(conn, c, hashed_string):
    c.execute("INSERT INTO hexcodes (hexcode_hash) VALUES (?)",(hashed_string, ))
    conn.commit()