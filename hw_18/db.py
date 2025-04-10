# Импортируем необходимые компоненты из SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# URL подключения к базе данных PostgreSQL
DB_URL = "postgresql://postgres:5093632@localhost:5432/events"

# Создаем базовый класс для декларативного определения моделей
Base = declarative_base()

# Создаем движок подключения к БД
engine = create_engine(DB_URL)

# Создаем фабрику сессий — через неё будет происходить работа с базой
Session = sessionmaker(bind=engine)

# ---------------------
# Определение моделей
# ---------------------

# Модель "Event" — мероприятие
class Event(Base):
    __tablename__ = 'events'  # Название таблицы в БД

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор (PRIMARY KEY)
    name = Column(String(100), unique=True, nullable=False)  # Название мероприятия, должно быть уникальным
    tickets = relationship("Ticket", back_populates="event")  # Связь "один ко многим" с таблицей Ticket


# Модель "Location" — город или место проведения
class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор
    city = Column(String(100), unique=True, nullable=False)  # Название города, тоже уникальное


# Модель "Ticket" — билет
class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор
    event_id = Column(Integer, ForeignKey('events.id', ondelete="CASCADE"))  # Внешний ключ на Event
    user_name = Column(String(255))  # Имя покупателя
    purchase_date = Column(DateTime(timezone=True), server_default=func.now())  # Дата и время покупки по умолчанию — текущая

    event = relationship("Event", back_populates="tickets")  # Обратная связь с Event


# ---------------------
# Функция для создания таблиц в БД
# ---------------------
def init_db():
    Base.metadata.create_all(engine)  # Создает все таблицы на основе описанных моделей


# ---------------------
# CRUD-функции для Event
# ---------------------

# Получить все мероприятия
def get_all_events():
    with Session() as session:
        return session.query(Event).all()  # SELECT * FROM events

# Создать новое мероприятие
def create_event(name):
    with Session() as session:
        event = Event(name=name)  # Создаем объект Event
        session.add(event)  # Добавляем в сессию
        session.commit()  # Подтверждаем транзакцию
        return event.id  # Возвращаем ID нового мероприятия

# Обновить мероприятие по ID
def update_event(event_id, new_name):
    with Session() as session:
        event = session.get(Event, event_id)  # Ищем мероприятие по ID
        if event:
            event.name = new_name  # Изменяем имя
            session.commit()  # Сохраняем изменения

# Удалить мероприятие по ID
def delete_event(event_id):
    with Session() as session:
        event = session.get(Event, event_id)
        if event:
            session.delete(event)
            session.commit()

# Поиск мероприятия по имени
def search_event_by_name(name):
    with Session() as session:
        return session.query(Event).filter(Event.name.ilike(f"%{name}%")).all()  # Поиск по части имени (без учета регистра)

# ---------------------
# CRUD-функции для Location
# ---------------------

# Получить все локации
def get_all_locations():
    with Session() as session:
        return session.query(Location).all()

# Создать новую локацию
def create_location(city):
    with Session() as session:
        location = Location(city=city)
        session.add(location)
        session.commit()
        return location.id

# Обновить локацию по ID
def update_location(location_id, new_city):
    with Session() as session:
        location = session.get(Location, location_id)
        if location:
            location.city = new_city
            session.commit()

# Удалить локацию
def delete_location(location_id):
    with Session() as session:
        location = session.get(Location, location_id)
        if location:
            session.delete(location)
            session.commit()

# ---------------------
# Билеты
# ---------------------

# Купить билет (создать запись)
def book_ticket(event_id, user_name):
    with Session() as session:
        ticket = Ticket(event_id=event_id, user_name=user_name)
        session.add(ticket)
        session.commit()
        return ticket.id

# Отменить билет
def cancel_ticket(ticket_id):
    with Session() as session:
        ticket = session.get(Ticket, ticket_id)
        if ticket:
            session.delete(ticket)
            session.commit()

# ---------------------
# Поиск по городу (опционально, если позже будут связи между Event и Location)
# ---------------------
def search_event_by_city(city):
    with Session() as session:
        return session.query(Event).join(Ticket).filter(Event.name.ilike(f"%{city}%")).all()
