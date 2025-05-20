from flask import Flask, render_template
from database import add_user
from flask import request


# Создание приложения
app = Flask(__name__)

# Обработка маршрута
# Обычная страница
@app.route("/")
def index():
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
        add_user(username, email, password, password2)
    return render_template("sing_up.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")
    
#запуск
app.run(debug=True)
