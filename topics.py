from db import db
import users
from sqlalchemy.sql import text
from datetime import datetime




def get_topics_id_content():
    sql = text("SELECT otp_topics.topic_id, otp_topics.topic_content FROM otp_topics, otp_users WHERE otp_topics.user_id = otp_users.user_id;")
    result = db.session.execute(sql)
    topics_id_content = result.fetchall()

    return topics_id_content




def get_topics_list():
    sql = text("SELECT otp_topics.topic_content, otp_users.username FROM otp_topics, otp_users WHERE otp_topics.user_id=otp_users.user_id ORDER BY otp_topics.topic_id DESC")
    result = db.session.execute(sql)
    topics_list = result.fetchall()
    return topics_list




def create_topic(topic, topic_comment):
    user_id = users.user_id()
    if user_id == 0:
        return False
    else:
        timestamp = datetime.now()  # Get the current timestamp

        sql = text("INSERT INTO otp_topics (topic_content, user_id) VALUES (:topic, :user_id) RETURNING topic_id")
        result = db.session.execute(sql, {"topic": topic, "user_id": user_id})  # Change "content" to "topic"
        topic_id_res = result.fetchone()

        sql = text("INSERT INTO otp_comments (user_id, comment_content, sent_at, topic_id) VALUES (:user_id, :topic_comment, :timestamp, :topic_id)")
        db.session.execute(sql, {"user_id": user_id, "topic_comment": topic_comment, "timestamp": timestamp, "topic_id": topic_id_res[0]})  # Change "content" to "topic_comment"
        db.session.commit()
        return True
