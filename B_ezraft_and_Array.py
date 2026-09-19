t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print(1)
    elif n == 2:
        print(-1)
    else:
        a = [1, 2, 3]
        s = 6

        while len(a) < n:
            a.append(s)
            s *= 2

        print(*a)
