import sqlite3

# Connecting database
def connect():
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookStore (id INTEGER PRIMARY KEY,title TEXT, author TEXT,year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

#--- Perform INSERT operation ---
def insert(title,author,year,isbn):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO bookStore VALUES(NULL, ?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

#--- Perform VIEW operation ---
def view():
    conn = sqlite3.connect("store.db")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM  bookStore")
    viewData = cur.fetchall()
    conn.close()
    return viewData

#--- Perform SELECT operation ---
def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect("store.db")
    cur  = conn.cursor()
    cur.execute("SELECT * FROM bookStore WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    searchData = cur.fetchall()
    conn.close()
    return searchData

#--- Perform DELETE operation ---
def delete(id):
    conn = sqlite3.connect("store.db")
    cur  = conn.cursor()
    cur.execute("DELETE FROM bookStore WHERE id=?",(id))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect("store.db")
    cur = conn.cursor()
    cur.execute("UPDATE bookStore SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()