import random

n = int(input("Введите целое число от 2 до 100: "))

# Проверяем, что n находится в допустимом диапазоне
if 2 <= n <= 100:
    # Создаем список из случайных целых чисел от 0 до 100
    random_numbers = [random.randint(0, 100) for _ in range(n)]

    # Инициализируем переменную для хранения суммы
    total = 0

    # Считаем сумму элементов списка без использования стандартных функций
    for number in random_numbers:
        total += number

    # Выводим сумму на экран
    print("Сумма всех элементов списка:", total)
else:
    print("Число должно быть от 2 до 100.")