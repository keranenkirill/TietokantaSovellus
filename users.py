from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import traceback




def login(username, password):
    sql = text("SELECT user_id, password FROM otp_users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.user_id
            session["username"] = username  # Store username in session
            print("no nut siis on sillee että ollaa avattu istunto", username, ":lle")
            return True
        else:
            return False




def logout():
    del session["user_id"]
    print("Logged out and session closed")




def register(firstname, lastname, age, city, username, password):
    print(firstname, lastname, age, city, username, password)
    hash_value = generate_password_hash(password)
    print(hash_value)
    try:
        # Check if the username already exists in the database
        user_query = text("SELECT user_id FROM otp_users WHERE username = :username")
        existing_user = db.session.execute(user_query, {"username": username}).fetchone()
        if existing_user:
            print("Username is already in use.")
            return False
        
        # If username is not in use, proceed with user registration
        insert_query = text("INSERT INTO otp_users (username, password, firstname, lastname, age, hometown) VALUES (:username, :password, :firstname, :lastname, :age, :hometown) RETURNING user_id")
        db.session.execute(insert_query, {"username": username, "password": hash_value, "firstname": firstname, "lastname": lastname, "age": age, "hometown": city})
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        print("Oops, something went wrong:")
        print(e)
        traceback.print_exc()
        return False
    
    print("vissii mennää return loginniin")
    return login(username, password)




def user_id():
    return session.get("user_id",0)