from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import traceback
#=============================================================================================================================================================


def login(username, password):
    sql = text("SELECT id, password FROM otp_users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            print("no nut siis on sillee että ollaa avattu istunto", username,":lle")
            return True
        else:
            return False
        


def logout():
    del session["user_id"]
    print("kirjauduttii ulos ja istunto suljettu")



def register(firstname, lastname, age, city, username, password):
    print(firstname, lastname, age, city, username, password)
    hash_value = generate_password_hash(password)
    print(hash_value)
    try:
        #lisätään dataa usr tauluun
        sql = text("INSERT INTO otp_users (username, password) VALUES (:username, :password) RETURNING id")#tässä palautamme id 
        result = db.session.execute(sql, {"username": username, "password": hash_value})#toteutetaan kysely 
        user_id = result.fetchone()[0]  #ja asetetaan id:n arvo muuttujan user_id arvoksi

        # lisätään dataa users_info tauluun käyttäen user_id viite avaimena
        #saatu user_id asetetaan tauluun
        sql = text("INSERT INTO otp_users_info (user_id, firstname, lastname, age, hometown) VALUES (:user_id, :firstname, :lastname, :age, :hometown)")
        db.session.execute(sql, {"user_id": user_id, "firstname": firstname, "lastname": lastname, "age": age, "hometown": city})

        db.session.commit()
    except Exception as e:
        print("Oops, something went wrong:")
        print(e)
        traceback.print_exc()
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)