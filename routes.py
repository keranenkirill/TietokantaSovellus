from app import app
from flask import render_template, request, redirect, url_for, session
import topics, users, comments, likes




@app.route("/")
def index():
   list = comments.get_topics_comment()
   for i in list:
       print(i)
   return render_template("index.html", count=len(list), messages=list)




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




@app.route("/send", methods=["POST"])
def send():
    topic_content = request.form["topic_content"]
    topic_comment = request.form["topic_comment"]
    error_messages = []

    if not topic_content:
        error_messages.append("topic content text area can't be empty")
    if not topic_comment:
        error_messages.append("topic comment text area can't be empty")
    if error_messages:
        return render_template("error.html", messages=error_messages)
    else:
        topics.create_topic(topic_content, topic_comment)
        return redirect("/")




@app.route("/add_topic_comment", methods=["POST"])
def add_comment():
    user_id = users.user_id()
    comment = request.form["topic_thread_comment"]
    topic_id = request.form["topic_id"]

    error_messages = []
    if not comment:
        error_messages.append("comment text area can't be empty")
        return render_template("error.html", messages=error_messages)

    # Add the comment to the database
    comments.insert_comment(user_id, comment, topic_id)

    # Redirect back to the thread page for the corresponding topic ID
    return redirect(url_for("topic_thread", id=topic_id))





@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO: show proper error if inserted wrong username fe. inserted username is not in database
            # show proper error if password incorrect for inserted username
            # show proper error if user did not insert username and password 

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            session['username'] = username 
            return redirect("/")
        else:
            return render_template("error.html", message="Incorrect username or password")




@app.route("/logout")
def logout():
    # TODO: show information, that user logged out and session deleted

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
        if not username:
            error_messages.append("Username is required")
        if password1 != password2:
            error_messages.append("Passwords do not match")
        if error_messages:
            return render_template("error.html", messages=error_messages)
        else:
            is_username_error = users.register(firstname, lastname, age, city, username, password1)
            if is_username_error == False:
                return render_template("error.html", messages=[is_username_error])  
            else:
                return redirect("/")
                
            

            