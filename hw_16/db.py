import psycopg2


DB_CONFIG = {
    "dbname": "events",
    "user": "postgres",
    "password": "5093632",
    "host": "localhost",
    "port": "5432"
}

def connect_db():
    return psycopg2.connect(**DB_CONFIG)

def init_db():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) UNIQUE
            );       
        """)

    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS location (
                id SERIAL PRIMARY KEY,
                city VARCHAR(100) UNIQUE
            );       
        """)

    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tickets (
                id SERIAL PRIMARY KEY,
                event_id INTEGER REFERENCES events(id) ON DELETE CASCADE,
                purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );       
        """)

def get_all_events():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events;")
        return cur.fetchall()

def get_all_locations():
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM locations;")
        return cur.fetchall

def create_event(name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO events (name) VALUES (%s)", (name,))

def update_event(event_id, new_name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE events SET name = %s WHERE id = %s;", (event_id, new_name))
        conn.commit()

def delete_event(event_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM events WHERE id = %s;", (event_id,))
        conn.commit()

def create_location(city):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO locations (city) VALUES (%s) RETURNING id;", (city,))
        location_id = cur.fetchone()[0]
        conn.commit()
        return location_id

def update_location(location_id, new_city):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("UPDATE locations SET city = %s WHERE id = %s;", (location_id,new_city))
        conn.commit()

def delete_location(location_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM locations WHERE id = %s;", (location_id,))
        conn.commit()

def search_event_by_name(name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events WHERE name ILIKE %s;", (f"%{name}%"))
        return cur.fetchall()

def search_event_by_city(city):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM events WHERE city ILIKE %s;", (f"%{city}%"))
        return cur.fetchall()

def search_event_by_location(location_name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("SELECT id, name, city FROM events WHERE city ILIKE %s;", (f"%{location_name}%",))
        return cur.fetchall()

def book_ticket(event_id, user_name):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO tickets (event_id, user_name) VALUES (%s, %s) RETURNING id;", (event_id, user_name))
        ticket_id = cur.fetchone()[0]
        conn.commit()
        return ticket_id


def cancel_ticket(ticket_id):
    with connect_db() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM tickets WHERE id = %s;", (ticket_id,))
        conn.commit()