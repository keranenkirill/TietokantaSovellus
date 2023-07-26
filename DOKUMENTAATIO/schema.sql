CREATE TABLE otp_users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    password TEXT NOT NULL,
    admin BOOLEAN NOT NULL DEFAULT FALSE
);



CREATE TABLE otp_users_info (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    age TEXT,
    hometown VARCHAR(100)
);