def cycle_row(row, count):
    while count > 0:
        for num in row:
            yield num
            count -= 1
            if count == 0:
                break

row = list(map(int, input("Введите числа для последовательности: ").split()))
count = int(input("Введите количество чисел: "))

print(*cycle_row(row, count))