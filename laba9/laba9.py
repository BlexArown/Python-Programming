from random import choice
def f(x):
    """Задайте функцию f(x), например, f(x) = x^2"""
    return x**2

def trapezoidal_method(a, b, N):
    """Реализация метода трапеций"""
    h = (b - a) / N  # Шаг разбиения
    result = 0.5 * (f(a) + f(b))  # Учет f0 и fN-1
    
    # Суммируем значения f(xi) для i от 1 до N-1
    for i in range(1, N-2):
        x = a + i * h
        result += f(x)
    
    result *= h  # Умножаем итог на шаг
    return result

# Параметры интегрирования
a = 0  # Начало интервала
b = 1  # Конец интервала

# Вычисляем интегралы для разных N
for N in [10, 100, 1000]:
    integral = trapezoidal_method(a, b, N)
    print(f"При N = {N}, приближенное значение интеграла: {integral:.6f}")
print("===============")
def is_magic_square(matrix):
    magic_sum = sum(matrix[0])
# Проверяем строки
    for row in matrix:
        if sum(row) != magic_sum:
            return False
# Проверяем столбцы
    for col in range(3):
        if sum(matrix[row][col] for row in range(3)) != magic_sum:
            return False
# Проверяем диагонали
    if sum(matrix[i][i] for i in range(3)) != magic_sum:
        return False
    if sum(matrix[i][2 - i] for i in range(3)) != magic_sum:
        return False
    return True

while True:
    m = []
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        m.append([0] * 3)
    for i in range(3):
        for j in range(3):
            m[i][j] = choice(number)
            number.remove(m[i][j])
    if is_magic_square(m):
        break


for i in range(3):
    for j in range(3):
        print(m[i][j], end=" ")
    print()
print('============')
treasure_count = int(input("Количество сокровищ:\n"))
treasure_coordinates_list = []

print("Координаты сокровищ:\n")
for i in range(treasure_count):
    treasure_coordinates = list(map(int, input().split()))
    treasure_coordinates_list.append(treasure_coordinates)

print("Координаты Александра:\n")
person_coordinates = list(map(int, input().split()))
closest = None
closest_sqr_distance = 9999999
for i in range(treasure_count):
    x_difference = person_coordinates[0] - treasure_coordinates_list[i][0]
    y_difference = person_coordinates[1] - treasure_coordinates_list[i][1]
    sqr_distance = x_difference**2 + y_difference**2
    if sqr_distance < closest_sqr_distance:
        closest = treasure_coordinates_list[i]
        closest_sqr_distance = sqr_distance
print(" ".join(map(str, closest)))
print("==========")
menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

# Функция для отображения одного блюда
def print_menu_item(item):
    print(f"Название: {item[0]}")
    print(f"Состав: {', '.join(item[1])}")
    print(f"Цена: {item[2]}")

# Функция для отображения всего меню
def print_menu(menu):
    print("Меню ресторана:")
    for i, item in enumerate(menu):
        print(f"{i + 1}. {item[0]} - {item[2]}$")
    print("\n")

# Функция для поиска блюда по названию
def find_menu_item_by_name(menu, name):
    filtered = list(filter(lambda x: x[0].lower().find(name.lower()) != -1, menu))
    if len(filtered) > 0:
        return filtered[0]
    else:
        return None

# Функция для добавления блюда
def add_menu_item(menu, name, ingredients, price):
    menu.append([name, ingredients, price])

# Ввод нового блюда
def input_menu_item(menu):
    name = input("Какое блюдо вы хотите добавить?\n> ")
    price = float(input("Сколько будет стоить блюдо?\n> "))
    ingredients_count = max(int(input("Сколько в блюде ингредиентов?\n> ")), 1)
    ingredients = []
    print("Введите ингредиенты:")
    for _ in range(ingredients_count):
        ingredients.append(input("> "))
    add_menu_item(menu, name, ingredients, price)

# Изменение цены блюда
def change_menu_item_price(menu, name, new_price):
    item = find_menu_item_by_name(menu, name)
    if item:
        item[2] = new_price
        print(f"Цена блюда '{item[0]}' обновлена на {new_price}$")
    else:
        print("Блюдо не найдено!")

# Основной цикл программы
while True:
    print("\n1. Показать меню")
    print("2. Найти блюдо по названию")
    print("3. Добавить новое блюдо")
    print("4. Изменить цену блюда")
    print("5. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        print_menu(menu)
    elif choice == "2":
        name = input("Введите название блюда: ")
        item = find_menu_item_by_name(menu, name)
        if item:
            print_menu_item(item)
        else:
            print("Блюдо не найдено!")
    elif choice == "3":
        input_menu_item(menu)
    elif choice == "4":
        name = input("Введите название блюда, цену которого хотите изменить: ")
        new_price = float(input("Введите новую цену: "))
        change_menu_item_price(menu, name, new_price)
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
print("=============")
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().split())  
transposed_matrix = [[None] * n for _ in range(m)]

for i in range(n):
    for j in range(m):
        transposed_matrix[j][i] = matrix[i][j]

for row in transposed_matrix:
    print(" ".join(row))
print("======")
n = int(input())

matrix = []
for _ in range(n):
    matrix.append(input().split())

new_matrix = [row[:] for row in matrix]

for i in range(n):
    new_matrix[i][i], new_matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]

for row in new_matrix:
    print(" ".join(row))
print("========")
[n, m] = list(map(int, input().split()))

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

k = int(input())
row = -1

for i in range(len(matrix)):
    current_max = 0
    count = 0
    prev = 0

    for j in range(len(matrix[0])):
        if prev == matrix[i][j]:
            count += 1
        else:
            count = 0

        if count > current_max:
            current_max = count

        prev = matrix[i][j]
    
    if (current_max + 1) >= k:
        row = i
        break

print(row + 1)
