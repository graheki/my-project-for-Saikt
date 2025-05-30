from flask import Flask, render_template
from database import add_user, log_in_user, add_message, get_msg
from flask import request


# Создание приложения
app = Flask(__name__)

# Обработка маршрута
# Обычная страница
@app.route("/", methods=['GET', 'POST'])
def index(): 

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Username: {username}, Password: {password}")
        log_in_user(username, password)

    return render_template("index.html")

# Страница о сайте
@app.route("/sing_up", methods=['GET', 'POST'])
def sing_up():

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        print(f"Username: {username}, Email: {email}, Password: {password} and {password2}")
        if password != password2:
            ...    
        else:
            for i in range(0, len(email)):
                if email[i] != "@":
                    ...
                else:
                    add_user(username, email, password, password2)
                    return render_template("index.html")
            
    return render_template("sing_up.html")

@app.route("/chat", methods=['GET', 'POST'])
def chat():

    if request.method == "POST":
        message_text = request.form["message"]
        add_message("Anonimus", message_text)

    msgs = get_msg()
    return render_template("chat.html", msgs=msgs)
    
#запуск
app.run(debug=True)
