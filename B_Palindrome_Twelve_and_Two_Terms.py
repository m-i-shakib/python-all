t = int(input())

for _ in range(t):
    n = int(input())

    if n == 10:
        print(-1)
    elif n % 12 == 10:
        print(22, n - 22)
    else:
        a = n % 12
        print(a, n - a)
