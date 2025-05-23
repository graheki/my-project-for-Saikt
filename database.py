import sqlite3 

def add_user(username, email, password, password2):
    conn = sqlite3.connect('gallery.db')

    cursor = conn.cursor()

    sql = "INSERT INTO user (login, email, password) VALUES (?, ?, ?)"

    cursor.execute(sql, (username, email, password))

    conn.commit()

    conn.close()

def log_in_user(username, password):
    conn = sqlite3.connect('gallery.db')

    cursor = conn.cursor()

    n = cursor.execute("SELECT login FROM User WHERE login = ", username)
    print(n)

    conn.commit()

    conn.close()

def add_message(name, msg):
    conn = sqlite3.connect('gallery.db')

    cursor = conn.cursor()

    sql = "INSERT INTO msg (name, text) VALUES (?, ?)"

    cursor.execute(sql, (name, msg))

    conn.commit()

    conn.close()

def get_msg():
    conn = sqlite3.connect('gallery.db')

    cursor = conn.cursor()

    sql = "SELECT * FROM msg"

    cursor.execute(sql)
    msgs = cursor.fetchall()

    conn.close()

    return msgs
