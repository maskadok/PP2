# 1
def squares(N):
    for i in range(N+1):
        yield i*i

for x in squares(5):
    print(x)
# 2
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
print(",".join(map(str, even_numbers(n))))
# 3
def divisible_numbers(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in divisible_numbers(n):
    print(num)
# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

for x in squares(1, 5):
    print(x)
# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input())
for num in countdown(n):
    print(num)