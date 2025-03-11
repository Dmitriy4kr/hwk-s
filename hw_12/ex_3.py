class Bus:
    def __init__(self, num_seats, max_speed, surnames, free_seats, bus_seats):
        self.num_seats = num_seats
        self.max_speed = max_speed
        self.surnames = surnames
        self.free_seats = free_seats
        self.bus_seats = bus_seats


    def boarding(self, name):
        if len(self.surnames) < self.num_seats:
            for seat, passenger in self.bus_seats.items():
                if passenger is None:
                    self.bus_seats[seat] = name
                    self.surnames.append(name)
                    print(f"{name} сел на место {seat}.")
                    return
        print(f"Нет свободных мест.")

    def off_boarding(self, name):
        if name in self.surnames:
            self.surnames.remove(name)
            for seat, passenger in self.bus_seats.items():
                if passenger == name:
                    self.bus_seats[seat] = None
                    print(f"{name} ушел с места {seat}.")
                    return
        print(f"{name} нет автобусе.")

    def current_speed(self):
        self.current_speed(0)

    def change_speed(self, new_speed):
        if 0 <= new_speed <= self.max_speed:
            self.current_speed = new_speed
            print(f"Скорость увеличена на {self.current_speed} км/ч.")
        else:
            print("Неправильное значение скорости.")

    def __contains__(self, name):
        return name in self.surnames


bus = Bus(num_seats=4, max_speed=80, surnames=[], free_seats=True, bus_seats={i: None for i in range(1, 5)})

bus.boarding("Сэндлер")
bus.boarding("Депп")
bus.boarding("Керри")
bus.boarding("Круз")
bus.boarding("Костнер")

print("Сэндлер" in bus)  # True
print("Депп" in bus)  # False

bus.off_boarding("Кэрри")
print("Костнер" in bus)  # False

bus.change_speed(50)


