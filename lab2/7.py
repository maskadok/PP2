x1 = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
y1 = int(input("Введите номер строки для первой клетки (от 1 до 8): "))
x2 = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
y2 = int(input("Введите номер строки для второй клетки (от 1 до 8): "))
if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")