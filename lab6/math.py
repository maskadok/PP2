# 1
import math
degree = float(input("Input degree: "))
radian = math.radians(degree)
print(f"Output radian: {radian:.6f}")
# 2
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))
area = ((base1 + base2) / 2) * height
print(f"Expected Output: {area}")
# 3
num_sides = int(input("Input number of sides: "))
length_side = float(input("Input the length of a side: "))
area = (num_sides * length_side ** 2) / (4 * math.tan(math.pi / num_sides))
print(f"The area of the polygon is: {area}")
# 4
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = base * height
print(f"Expected Output: {area:.1f}")