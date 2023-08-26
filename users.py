from db import db
from flask import session, flash
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



#TODO: update fname, lname, city, age and username into db columns by user_id
def update_users_fname(user_id, fnm): 
    upd_usr_fnm = text("UPDATE otp_users SET firstname = :firstname WHERE user_id = :user_id")
    db.session.execute(upd_usr_fnm, {"user_id": user_id, "firstname": fnm})
    db.session.commit()

def update_users_lname(user_id, lnm):
    upd_usr_lnm = text("UPDATE otp_users SET lastname = :lastname WHERE user_id = :user_id")
    db.session.execute(upd_usr_lnm, {"user_id": user_id, "lastname": lnm})
    db.session.commit()

def update_users_city(user_id, cty):
    upd_usr_cty = text("UPDATE otp_users SET hometown = :hometown WHERE user_id = :user_id")
    db.session.execute(upd_usr_cty, {"user_id": user_id, "hometown": cty})
    db.session.commit()

def update_users_age(user_id, age):
    upd_usr_age = text("UPDATE otp_users SET age = :age WHERE user_id = :user_id")
    db.session.execute(upd_usr_age, {"user_id": user_id, "age": age})
    db.session.commit()

def update_users_usrnm(user_id, usrnm):
    user_query = text("SELECT user_id FROM otp_users WHERE username = :username")
    existing_user = db.session.execute(user_query, {"username": usrnm}).fetchone()
    if existing_user:
        flash("Username is already in use.")
    else:
        try:
            upd_usr_usrnm = text("UPDATE otp_users SET username = :username WHERE user_id = :user_id")
            db.session.execute(upd_usr_usrnm, {"user_id": user_id, "username": usrnm})
            db.session.commit()
            session["username"] = usrnm
        except Exception as e:
            print("An error occurred:", str(e))





def user_information(user_id):

    # Retrieve all user information using the user_id
    user_info_query = text("SELECT username, user_id, age, hometown, firstname, lastname FROM otp_users WHERE user_id = :user_id")
    user_info = db.session.execute(user_info_query, {"user_id": user_id}).fetchall()

    return user_info
    #else:
       # print("User information not found.")



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