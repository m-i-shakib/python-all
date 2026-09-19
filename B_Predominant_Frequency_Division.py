t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)

    for i in range(n):
        pref1[i + 1] = pref1[i] + (1 if a[i] == 1 else -1)
        pref2[i + 1] = pref2[i] + (-1 if a[i] == 3 else 1)

    mn = 10**9
    ok = False

    for i in range(1, n):
        if pref2[i] >= mn:
            ok = True
            break

        if pref1[i] >= 0:
            mn = min(mn, pref2[i])

    print("YES" if ok else "NO")
