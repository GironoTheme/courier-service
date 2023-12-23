INSERT INTO posts(name)
VALUES('Администратор'), ('Курьер'), ('Клиент');

INSERT INTO users(login, password, post_id)
VALUES ('admin', 'admin', 1);

INSERT INTO orders(id, name_of_order, price)
VALUES (1, 'Козинаки', '200'), (2, 'Бишпармак', '250'), (3, 'Онигири', '150');

INSERT INTO workers(id, surname, name, salary, work_experience)
VALUES(1, 'Иванов', 'Иван', "20000", "1 год"), (2, 'Петров', 'Петр', "25000", "2 года"), (3, 'Сидоров', 'Сидр', "28000", "3 года");

