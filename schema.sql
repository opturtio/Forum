DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS topics CASCADE;
DROP TABLE IF EXISTS messages CASCADE;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
)

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    topic TEXT UNIQUE,
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    topic_id TEXT REFERENCES topics
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

