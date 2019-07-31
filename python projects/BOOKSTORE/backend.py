import sqlite3

def connect():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("create table if NOT exists book (id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("insert into book values(null,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

insert("global price","s.k yadav",2010,15)

def view():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book")
    row = cur.fetchall()
    conn.close()
    return row


def search(title="",author="",year="",isbn=""):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("select * from book where title=? OR author =? OR year = ? OR isbn=? ",(title,author,year,isbn))
    row = cur.fetchall()
    conn.close()
    return row

def delete(id):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("delete from book where id=?",(id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("update book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()


print(view())
update(3,"python raja","sachin kumar",2101,1223)

print(view())














