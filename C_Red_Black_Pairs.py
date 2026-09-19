t = int(input())

for _ in range(t):
    n = int(input())

    a = input().strip()
    b = input().strip()

    d = [0] * (n + 1)

    d[1] = int(a[0] != b[0])

    for i in range(2, n + 1):
        v = d[i - 1] + (a[i - 1] != b[i - 1])

        h = d[i - 2] + (a[i - 2] != a[i - 1]) + (b[i - 2] != b[i - 1])

        d[i] = min(v, h)

    print(d[n])
