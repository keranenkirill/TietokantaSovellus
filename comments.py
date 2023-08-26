from db import db
from sqlalchemy.sql import text


#return all topics on mainpage, showing only first comment for each topic
# first comment is comment that made by topic creator
def get_topics_comment():
    sql = text("SELECT DISTINCT ON (t.topic_id) t.topic_id, t.topic_content, c.comment_content, u.username FROM otp_topics t JOIN otp_comments c ON t.topic_id = c.topic_id JOIN otp_users u ON c.user_id = u.user_id ORDER BY t.topic_id DESC, c.comment_id")
    result = db.session.execute(sql) 
    topic_comment = result.fetchall()
    return topic_comment


def insert_comment(user_id, comment_content, topic_id):
    sql = text("INSERT INTO otp_comments (user_id, comment_content, sent_at, topic_id) VALUES (:user_id, :comment_content, NOW(), :topic_id);")
    db.session.execute(sql, {"user_id": user_id, "comment_content": comment_content, "topic_id": topic_id})
    db.session.commit()

#lists all all comments, first comment on top 
def get_all_comments_by_topic(topic_id):
    sql = text("SELECT c.comment_content, u.username, c.comment_id, c.likes FROM otp_comments c JOIN otp_users u ON c.user_id = u.user_id JOIN otp_topics t ON c.topic_id = t.topic_id WHERE t.topic_id = :topic_id ORDER BY c.comment_id;")
    result = db.session.execute(sql, {"topic_id": topic_id}) 
    comments_list = result.fetchall()
    return comments_list


def get_all_comments_by_userid(user_id):
    sql = text("SELECT c.topic_id, c.comment_content FROM otp_users u JOIN otp_comments c ON u.user_id = c.user_id WHERE u.user_id = :user_id;")
    result = db.session.execute(sql, {"user_id": user_id}) 
    users_comments_list = result.fetchall()
    return users_comments_list