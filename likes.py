from db import db
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

#This function ensures that the user can only give a like or dislike once.
def add_reaction(user_id, comment_id, increment_value):
    try:
        with db.session.begin():
            # Check if the user has already reacted to this comment
            existing_reaction = db.session.execute(
                text("SELECT reaction_type FROM otp_user_reactions WHERE user_id = :user_id AND comment_id = :comment_id"),
                {'user_id': user_id, 'comment_id': comment_id}
            ).fetchone()

            # Determine the current reaction type
            current_reaction_type = existing_reaction[0] if existing_reaction else None

            # Determine the new reaction type based on increment_value
            if increment_value == 1:
                new_reaction_type = 'like'
            elif increment_value == -1:
                new_reaction_type = 'dislike'
            else:
                raise ValueError("Invalid increment_value")

            # Increment or decrement likes in otp_comments table based on the change in reaction type
            if current_reaction_type is None:
                likes_change = increment_value
            elif current_reaction_type == 'like' and new_reaction_type == 'dislike':
                likes_change = -1
            elif current_reaction_type == 'dislike' and new_reaction_type == 'like':
                likes_change = 1
            else:
                likes_change = 0  # No change in likes

            if likes_change != 0:
                update_sql = text("UPDATE otp_comments SET likes = likes + :likes_change WHERE comment_id = :comment_id")
                db.session.execute(update_sql, {'likes_change': likes_change, 'comment_id': comment_id})

            # Insert or update reaction in otp_user_reactions table
            if existing_reaction:
                update_sql = text("UPDATE otp_user_reactions SET reaction_type = :new_reaction_type WHERE user_id = :user_id AND comment_id = :comment_id")
                db.session.execute(update_sql, {'new_reaction_type': new_reaction_type, 'user_id': user_id, 'comment_id': comment_id})
            else:
                insert_sql = text("INSERT INTO otp_user_reactions (user_id, comment_id, reaction_type) VALUES (:user_id, :comment_id, :new_reaction_type)")
                db.session.execute(insert_sql, {'user_id': user_id, 'comment_id': comment_id, 'new_reaction_type': new_reaction_type})
            
            return True

    except SQLAlchemyError as e:
        db.session.rollback()
        raise e

def add_like(user_id, comment_id):
    add_reaction(user_id, comment_id, 1)

    #DEBUG LINES BELOW:
    #added = add_reaction(user_id, comment_id, 1)
    #if added:
    #    return print("Liked successfully")
    #else:
    #    return print("Already liked")

def add_dislike(user_id, comment_id):
    add_reaction(user_id, comment_id, -1)

    #DEBUG LINES BELOW:
    #added = add_reaction(user_id, comment_id, -1)
    #if added:
    #    return print("Disliked successfully")
    #else:
    #    return print("Already disliked")