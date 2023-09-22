x1, y1, x2, y2 = input("Введите координаты двух клеток (чередующиеся числа от 1 до 8): ").split()
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
if (x1 + y1) % 2 == (x2 + y2) % 2:
    print("YES")
else:
    print("NO")