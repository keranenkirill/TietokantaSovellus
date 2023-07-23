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
            return render_template("error.html", message="Incorrect username or password")


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
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        age = request.form["age"]
        city = request.form["city"]
        
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        error_messages = []

        if not firstname:
            error_messages.append("First name is required")
        
        if not lastname:
            error_messages.append("Last name is required")
        
        if not age:
            error_messages.append("Age is required")
        else:
            try:
                age = int(age)
            except ValueError:
                error_messages.append("Age must be a number")
        
        if not city:
            error_messages.append("City is required")

        if password1 != password2:
            error_messages.append("Passwords do not match")

        if error_messages:
            return render_template("error.html", messages=error_messages)
        else:
            if users.register(firstname, lastname, age, city, username, password1):
                return redirect("/")
            else:
                return render_template("error.html", messages=["Registration failed"])