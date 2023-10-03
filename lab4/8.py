maxnum = int(input())
possiblenums = set(range(1, maxnum + 1))

while True:
    try:
        line = input().split()
        if line[0] == "HELP":
            break
        question_set = set(int(x) for x in line)
        intersection = possiblenums & question_set
        if len(intersection) == len(possiblenums) // 2:
            answer = "NO"
        else:
            answer = "YES"
        print(answer)
        if answer == "NO":
            possiblenums -= question_set
        elif answer == "YES":
            possiblenums &= question_set
    except error:
        break
result = sorted(possiblenums)
print(*result)