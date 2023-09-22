n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))
k = int(input("Введите количество долек (k): "))
if k <= n * m and (k % n == 0 or k % m == 0):
    print("YES")
else:
    print("NO")