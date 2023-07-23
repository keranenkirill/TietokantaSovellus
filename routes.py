from app import app
from flask import render_template, request, redirect
import users


@app.route("/")
def index():
   return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana")


@app.route("/logout")
def logout():
    users.logout()
    print("suljettii sessio ja nyt redirect /-sivulle")
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        city = request.form["city"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        error_messages = []

        if not age:
            error_messages.append("Ikä-kenttä on pakollinen")
        else:
            try:
                age = int(age)
            except ValueError:
                error_messages.append("Ikä-kentän pitää olla numero")
        
        if not city:
            error_messages.append("Kaupunki-kenttä on pakollinen")

        if password1 != password2:
            error_messages.append("Salasanat eroavat")

        if error_messages:
            return render_template("error.html", messages=error_messages)
        else:
            if users.register(username, age, city, password1):
                return redirect("/")
            else:
                return render_template("error.html", messages=["Rekisteröinti ei onnistunut"])