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

    print(cursor.fetchone(1))

    conn.commit()

    conn.close()