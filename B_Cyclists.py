t = int(input())

for _ in range(t):
    n, k, p, m = map(int, input().split())

    a = list(map(int, input().split()))

    win = a[p - 1]

    f = 0

    if p > k:
        b = a[: p - 1]

        b.sort()

        need = p - k

        for i in range(need):
            f += b[i]

    b = []

    for i in range(n):
        if i != p - 1:
            b.append(a[i])

    b.sort()

    again = 0

    need = n - k

    for i in range(need):
        again += b[i]

    first_c = f + win

    if first_c > m:
        print(0)

    else:
        m = m - first_c

        ans = 1

        cost = again + win

        ans = ans + (m // cost)

        print(ans)
