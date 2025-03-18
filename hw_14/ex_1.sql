CREATE DATABASE HW14;

CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,
    Name VARCHAR,
    Position VARCHAR,
    Department VARCHAR,
    Salary INT
);

INSERT INTO Employees (Name, Position, Department, Salary) VALUES
('Джонни Депп', 'Актер', 'Маркетинг', 3500),
('Адам Сэндлер', 'Художник', 'Творческий отдел', 5000),
('Крис Рок', 'Комик', 'Творческий отдел', 4000),
('Кевин Костнер', 'Ковбой', 'Курьерская служба', 3000),
('Киану Ривз', 'Охранник', 'Служба безопасности', 2500);

UPDATE Employees
SET Position = 'Руководитель Курьерской службы'
WHERE Name = 'Кевин Костнер';

UPDATE Employees
SET Salary = '3500'
WHERE Name = 'Кевин Костнер';

UPDATE Employees
SET Position = 'Начальник охраны'
WHERE Name = 'Киану Ривз';

ALTER TABLE Employees
ADD COLUMN HireDate DATE;

UPDATE Employees
SET HireDate = CASE
    WHEN Name = 'Джонни Депп' THEN '2020-03-18'
    WHEN Name = 'Адам Сэндлер' THEN '2021-04-21'
    WHEN Name = 'Крис Рок' THEN '2023-05-25'
    WHEN Name = 'Кевин Костнер' THEN '2010-10-29'
    WHEN Name = 'Киану Ривз' THEN '2022-06-11'
    ELSE HireDate
END;

SELECT * FROM Employees
WHERE Position = 'Комик';

SELECT * FROM Employees
WHERE Salary > '3400';

SELECT * FROM Employees
WHERE Department = 'Творческий отдел';

SELECT ROUND(AVG(Salary), 2) AS Average
FROM Employees;

DROP TABLE Employees;