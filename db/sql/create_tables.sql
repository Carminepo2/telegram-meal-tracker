
CREATE TABLE IF NOT EXISTS meals
(
    id TEXT UNIQUE,
    user_chat_id INTEGER,
    content TEXT,
    calories INTEGER,
    consumed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS users
(
    chat_id INTEGER UNIQUE,
    name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY(chat_id)
);