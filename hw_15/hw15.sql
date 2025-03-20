CREATE TABLE authors(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    author_id INTEGER REFERENCES authors(id),
    publication_year INT
);

CREATE TABLE sales(
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    quantity INT
);

INSERT INTO authors (first_name, last_name) VALUES
('Владимир', 'Маяковский'),
('Владимир', 'Высоцкий'),
('Михаил', 'Лермонтов'),
('Фёдор', 'Достоевский'),
('Иван', 'Мележ'),
('Якуб', 'Колас');

INSERT INTO books (title, author_id, publication_year) VALUES
('Во весь голос', 1, 1930),
('Баллада о любви', 2, 1972),
('Мцыри', 3, 1840),
('Преступление и наказание', 4, 1866),
('Людзі на балоце', 5, 1966),
('Война и Мир', NULL, 1867);

INSERT INTO sales (book_id, quantity) VALUES
(1, 25),
(2, 32),
(3, 14),
(4, 48),
(5, 12);

SELECT b.title, a.first_name, a.last_name
FROM books b
INNER JOIN authors a ON b.author_id = a.id

SELECT a.first_name, a.last_name, b.title
FROM authors a
LEFT JOIN books b ON b.author_id = a.id;

SELECT b.title, a.first_name, a.last_name
FROM books b
RIGHT JOIN authors a ON b.author_id = a.id

SELECT a.first_name, a.last_name, b.title, b.publication_year, c.quantity
FROM authors a
INNER JOIN books b ON b.author_id = a.id
INNER JOIN sales c ON b.id = c.book_id;

SELECT a.first_name, a.last_name, b.title, c.quantity
FROM authors a
FULL OUTER JOIN books b ON b.author_id = a.id
LEFT JOIN sales c ON c.book_id = b.id


