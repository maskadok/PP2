x = float(input("Введите число x: "))
if x > 0:
    sign_x = 1
elif x < 0:
    sign_x = -1
else:
    sign_x = 0
print("Знак числа x:", sign_x)