import sqlite3

def connect():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS contacts (id INTEGER PRIMARY KEY, name TEXT, address TEXT, mobile INTEGER, email TEXT)")
    conn.commit()
    conn.close()

def insert(name, address, mobile, email):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO contacts VALUES (NULL, ?,?,?,?)", (name,address,mobile,email))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(name="", address="", mobile="", email=""):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name=? OR address=? OR mobile=? OR email=?", (name, address, mobile, email))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update(id,name,address,mobile,email):
    conn=sqlite3.connect("contacts.db")
    cur=conn.cursor()
    cur.execute("UPDATE contacts SET name=?, address=?, mobile=?, email=? WHERE id=?", (name,address,mobile,email,id))
    conn.commit()
    conn.close()

connect()
