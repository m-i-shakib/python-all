t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    p = [0] * k

    for i in range(n):
        if s[i] == "1":
            p[i % k] ^= 1

    print("YES" if not any(p) else "NO")
