CREATE TABLE otp_users
(
  user_id SERIAL PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  password TEXT NOT NULL,
  admin BOOL NOT NULL DEFAULT FALSE,
  firstname VARCHAR(50) NOT NULL,
  lastname VARCHAR(50) NOT NULL,
  hometown VARCHAR(75),
  age INT NOT NULL
);

CREATE TABLE otp_topics
(
  topic_id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  topic_content VARCHAR(100) NOT NULL,
  postable BOOL,
  FOREIGN KEY (user_id) REFERENCES otp_users(user_id)
);

CREATE TABLE otp_comments
(
  comment_id SERIAL PRIMARY KEY,
  user_id INT NOT NULL,
  comment_content VARCHAR(200) NOT NULL,
  sent_at TIMESTAMP NOT NULL,
  topic_id INT NOT NULL,
  visible BOOL DEFAULT TRUE,
  likes INT DEFAULT 0,
  FOREIGN KEY (user_id) REFERENCES otp_users(user_id),
  FOREIGN KEY (topic_id) REFERENCES otp_topics(topic_id)
);

CREATE TABLE otp_user_reactions
(
  user_id INT,
  comment_id INT,
  reaction_type VARCHAR(10), 
  PRIMARY KEY (user_id, comment_id),
  FOREIGN KEY (user_id) REFERENCES otp_users(user_id),
  FOREIGN KEY (comment_id) REFERENCES otp_comments(comment_id)
);

