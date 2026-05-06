t = int(input())
for _ in range(t):
    s = int(input())
    digits = ""
    for d in range(9, 0, -1):
        if s >= d:
            digits += str(d)
            s -= d
    print(digits[::-1])
