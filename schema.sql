DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS topics CASCADE;
DROP TABLE IF EXISTS messages CASCADE;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE IF NOT EXISTS topics (
    id SERIAL PRIMARY KEY,
    topic TEXT UNIQUE,
    user_id INTEGER REFERENCES users,
    posts INTEGER,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    content TEXT,
    topic_id INTEGER REFERENCES topics,
    user_id INTEGER REFERENCES users,
    created_at TIMESTAMP
);

