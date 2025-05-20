def add_user(username, email, password, password2):
    conn = sqlite3.connect('gallery.db')

    cursor = conn.cursor()

    sql = "INSERT INTO user (username, email, password) VALUES (?, ?, ?)"

    cursor.execute(sql, (username, email, password))

    conn.commit()

    conn.close()

