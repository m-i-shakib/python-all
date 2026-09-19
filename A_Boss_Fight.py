from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = Counter(a)
    total = sum(a)

    value, mx = max(cnt.items(), key=lambda x: x[1])
    others = n - mx

    if mx <= others + 2:
        print(total)
    else:
        print(total - (mx - others - 2) * value)
