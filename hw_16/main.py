import db


def print_menu():
    print("Выберите действие:")
    print("0. Выход")
    print("1. Показать мероприятия")
    print("2. Показать города проведения мероприятий")
    print("3. Добавить новое мероприятие")
    print("4. Изменить мероприятие")
    print("5. Удалить мероприятие")
    print("6. Добавить город")
    print("7. Изменить город")
    print("8. Удалить город")
    print("9. Поиск мероприятия по городу проведения")
    print("10. Поиск мероприятия по его названию")
    print("11. Поиск мероприятия по городу проведения")
    print("12. Забронировать билет")
    print("13. Отменить бронь билета")

def app():
    db.init_db()
    print("База данных определена.")

    while True:
        print_menu()
        cmd = input("Введите команду: ")

        if cmd == "0":
            print("Досвидос!")
            break

        elif cmd == "1":
            print("=" * 20)
            print("Список мероприятий:")
            events = db.get_all_events()
            for event in events:
                print(f"ID: {event[0]} | Название: {event[1]} |")
            print("=" * 20)

        elif cmd == "2":
            print("=" * 20)
            print("Список всех локаций:")
            locations = db.get_all_locations()
            for loc in locations:
                print(f"ID: {loc[0]} | Город: {loc[1]}")
            print("=" * 20)

        elif cmd == "3":
            print("=" * 20)
            name = input("Введите название мероприятия: ")
            event_id = db.create_event(name)
            print(f"Мероприятие добавлено с ID {event_id}.")
            print("=" * 20)

        elif cmd == "4":
            print("=" * 20)
            event_id = int(input("Введите ID мероприятия: "))
            new_name = input("Введите новое название: ")
            db.update_event(event_id, new_name)
            print("Мероприятие обновлено.")
            print("=" * 20)

        elif cmd == "5":
            print("=" * 20)
            event_id = int(input("Введите ID мероприятия для удаления: "))
            db.delete_event(event_id)
            print("Мероприятие удалено.")
            print("=" * 20)

        elif cmd == "6":
            print("=" * 20)
            city = input("Введите название нового города: ")
            loc_id = db.create_location(city)
            print(f"Локация добавлена с ID {loc_id}.")
            print("=" * 20)

        elif cmd == "7":
            print("=" * 20)
            loc_id = int(input("Введите ID локации: "))
            new_city = input("Введите новое название города: ")
            db.update_location(loc_id, new_city)
            print("Локация обновлена.")
            print("=" * 20)

        elif cmd == "8":
            print("=" * 20)
            loc_id = int(input("Введите ID локации для удаления: "))
            db.delete_location(loc_id)
            print("Локация удалена.")
            print("=" * 20)

        elif cmd == "9":
            print("=" * 20)
            city = input("Введите город для поиска мероприятий: ")
            events = db.search_event_by_city(city)
            if events:
                print(f"Мероприятия в городе {city}:")
                for e in events:
                    print(f"ID: {e[0]} | Название: {e[1]}")
            else:
                print(f"Мероприятий в городе {city} не найдено.")
            print("=" * 20)

        elif cmd == "10":
            print("=" * 20)
            name = input("Введите название мероприятия: ")
            results = db.search_event_by_name(name)
            if results:
                for res in results:
                    print(f"ID: {res[0]} | Название: {res[1]} | Город: {res[2]}")
            else:
                print("Мероприятие не найдено.")
            print("=" * 20)

        elif cmd == "11":
            print("=" * 20)
            location_name = input("Введите название места проведения (города): ")
            events = db.search_event_by_city(location_name)
            if events:
                print(f"Мероприятия в локации '{location_name}':")
                for e in events:
                    print(f"ID: {e[0]} | Название: {e[1]}")
            else:
                print(f"Мероприятий в локации '{location_name}' не найдено.")
            print("=" * 20)

        elif cmd == "12":
            print("=" * 20)
            event_id = int(input("Введите ID мероприятия: "))
            user_name = input("Введите ваше имя: ")
            ticket_id = db.book_ticket(event_id, user_name)
            print(f"Билет забронирован под номером {ticket_id}.")
            print("=" * 20)

        elif cmd == "13":
            print("=" * 20)
            ticket_id = int(input("Введите ID билета для отмены: "))
            db.cancel_ticket(ticket_id)
            print(f"Бронирование билета с ID {ticket_id} отменено.")
            print("=" * 20)

        else:
            print("Неверная команда. Попробуйте снова.")

app()