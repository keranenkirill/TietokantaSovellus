from app import app
from flask import render_template, request, redirect, url_for, session, flash
import topics, users, comments, likes




@app.route("/")
def index():
    comments_list = comments.get_topics_comment()
    return render_template("index.html", count=len(comments_list), messages=comments_list)



@app.route("/thread/<id>")
def topic_thread(id):
    topics_id_content = topics.get_topics_id_content()
    topic_content = None

    for topic_id, content in topics_id_content:
        if str(topic_id) == id:
            topic_content = content
            break

    comments_list = comments.get_all_comments_by_topic(int(id))
    return render_template("thread.html", topic_id=str(id), content=topic_content, comments=comments_list)



@app.route("/like_comment", methods=["POST"])
def like_comment():
    user_id = session.get("user_id") 
    topic_id = request.form["topic_id"]
    comment_id = request.form["comment_id"]
    like = request.form.get("like")  
    dislike = request.form.get("dislike")

    if like:
        likes.add_like(user_id, comment_id)
    elif dislike:
        likes.add_dislike(user_id, comment_id)

    return redirect(url_for("topic_thread", id=topic_id))



@app.route("/<usrnm>")
def userpage(usrnm):
    usrnm = session.get("username")
    user_id = session.get("user_id")

    #return all user information about user who is currently logged in (age, f.name, l.name, homecity)
    user_info_list = users.user_information(user_id)
    users_topics_list = topics.get_all_topics_by_userid(user_id)
    users_comments_list = comments.get_all_comments_by_userid(user_id)

    return render_template("users_page.html", users_info=user_info_list, users_comments=users_comments_list, users_topics=users_topics_list)



@app.route("/send", methods=["POST"])
def send():
    topic_content = request.form["topic_content"]
    topic_comment = request.form["topic_comment"]

    if not topic_content:
        flash("Topic content text area can't be empty", "error")
    if not topic_comment:
        flash("Topic comment text area can't be empty", "error")
    
    if not topic_content or not topic_comment:
        return redirect("/")
    
    topics.create_topic(topic_content, topic_comment)
    return redirect("/")



@app.route("/add_topic_comment", methods=["POST"])
def add_comment():
    #TODO: ERROR handling
    user_id = users.user_id()
    comment = request.form["topic_thread_comment"]
    topic_id = request.form["topic_id"]

    if not comment:
        flash("comment text area can't be empty")
        return redirect(url_for("topic_thread", id=topic_id))
    else:
        # Add the comment to the database
        comments.insert_comment(user_id, comment, topic_id)
        # Redirect back to the thread page for the corresponding topic ID
        return redirect(url_for("topic_thread", id=topic_id))



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            session['username'] = username
        else:
            flash('Invalid username or password')

    return redirect("/")



@app.route("/logout")
def logout():
    users.logout()
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

        if not firstname or firstname == '':
            flash("First name is required")
        if not lastname or lastname == '':
            flash("Last name is required")
        if not age or age == '':
            flash("Age is required")
        else:
            try:
                age = int(age)
            except ValueError:
                flash("Age must be a number")
        if not city or city == '':
            flash("City is required")
        if not username or username == '':
            flash("Username is required")
        if not password1 or password1 == '':
            flash("Password is required")
        if not password2 or password2 == '':
            flash("Password is required")
        if password1 != password2:
            flash("Passwords do not match")
        else:
            registration_result = users.register(firstname, lastname, age, city, username, password1)
            if registration_result == False:
                
                flash(registration_result)
                return render_template("register.html")
            if registration_result == True:
                print("Successfully registered:", username)
                return render_template("index.html")



@app.route("/upd_user_info", methods=["POST"])
def upd_usr_info():
    user_id = users.user_id()

    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    city = request.form["city"]
    age = request.form["age"]
    username = request.form["username"]

    if firstname: users.update_users_fname(user_id, firstname)
    else: pass

    if lastname: users.update_users_lname(user_id, lastname)
    else: pass

    if city: users.update_users_city(user_id, city)
    else: pass

    if age: users.update_users_age(user_id, age)
    else: pass

    if username: users.update_users_usrnm(user_id, username)
    else: pass
    
    usrnm = session.get("username")
    return userpage(usrnm)
