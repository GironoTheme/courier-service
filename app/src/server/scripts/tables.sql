CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100)
);

CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login VARCHAR(100),
    password VARCHAR(100),
    post_id INTEGER,
    reg_date INT NOT NULL DEFAULT (strftime('%s','now')),
    FOREIGN KEY(post_id)
        REFERENCES posts(id)
            ON DELETE NO ACTION
);

CREATE TABLE orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name_of_orders VARCHAR(100)
    price INTEGER
);

CREATE TABLE workers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    surname VARCHAR(100),
    name VARCHAR(100),
    salary INTEGER,
    work_experience VARCHAR(100)
);

