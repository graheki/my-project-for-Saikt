from flask import Flask, render_template

# Создание приложения
app = Flask(__name__)

# Обработка маршрута
# Обычная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница о сайте
@app.route("/about")
def about():
    return render_template("about.html")

#запуск
app.run(debug=True)
