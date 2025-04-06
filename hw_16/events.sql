CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,                   -- Уникальный идентификатор локации
    city VARCHAR(100) UNIQUE NOT NULL        -- Локация (город)
);

CREATE TABLE IF NOT EXISTS events (
    id SERIAL PRIMARY KEY,                   -- Уникальный идентификатор мероприятия
    name VARCHAR(100) UNIQUE,
    location_id INT REFERENCES locations(id) ON DELETE CASCADE                 -- Название мероприятия
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,                                  -- Уникальный идентификатор билета                             -- Ссылка на мероприятие
    event_id INT REFERENCES events(id) ON DELETE CASCADE,                             -- Ссылка на конкретное место
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_name VARCHAR(100)              -- Дата и время бронирования
);