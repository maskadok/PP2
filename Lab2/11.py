x1 = int(input("Введите номер столбца для первой клетки (от 1 до 8): "))
y1 = int(input("Введите номер строки для первой клетки (от 1 до 8): "))
x2 = int(input("Введите номер столбца для второй клетки (от 1 до 8): "))
y2 = int(input("Введите номер строки для второй клетки (от 1 до 8): "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("YES")
else:
    print("NO")