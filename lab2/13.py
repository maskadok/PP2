N = int(input("Введите длину бассейна (N): "))
M = int(input("Введите ширину бассейна (M): "))
x = int(input("Введите расстояние до длинного бортика (x): "))
y = int(input("Введите расстояние до короткого бортика (y): "))
min_distance = min(x, y, N - x, M - y)
print("Минимальное расстояние до бортика:", min_distance)