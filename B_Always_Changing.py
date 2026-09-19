t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    n0 = s.count("0")
    n1 = n - n0

    delta_n = n0 - n1

    if abs(delta_n) > 2:
        print(-1)
        continue

    L = 1
    L0 = 1 if s[0] == "0" else 0
    L1 = 1 if s[0] == "1" else 0

    for i in range(1, n):
        if s[i] != s[i - 1]:
            L += 1

            if s[i] == "0":
                L0 += 1
            else:
                L1 += 1

    delta_L = L0 - L1

    ans = (n - L) + max(0, abs(delta_n - delta_L) - 1)

    print(ans)
