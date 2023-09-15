# Вводим значения a, b, l и N
a = int(input())
b = int(input())
l = int(input())
N = int(input())
length_of_laces = b * (N - 1) * 2 + a * ((N - 1) * 2 + 1) + l * 2
print(length_of_laces)
