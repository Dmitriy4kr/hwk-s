def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

num = int(input("Введите количество чисел Фибоначчи: "))

print(*fibonacci(num))