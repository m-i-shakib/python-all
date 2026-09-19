t = int(input())

for _ in range(t):
    n = int(input())

    a = []

    for i in range(n):
        x = 2 * i + 1
        a.append(x * (x + 2))

    print(*a)
