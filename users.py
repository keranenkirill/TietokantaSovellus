from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text



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




def register(username, age, city, password):
    print(username, password)
    hash_value = generate_password_hash(password)
    print(hash_value)
    try:
        sql = text("INSERT INTO otp_users (username, age, city, password) VALUES (:username,:age,:city,:password)")
        db.session.execute(sql, {"username":username, "age":age, "city":city, "password":hash_value})
        db.session.commit()
    except:
        print("ollaa falses ja kuulemma sen takia että tunnus jo käytössä tai jokun muu syy")
        return False
    return login(username, password)

def user_id():
    return session.get("user_id",0)