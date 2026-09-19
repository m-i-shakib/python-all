t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    left = -1
    best_l = -1
    best_r = -1
    best_len = 0

    for i in range(n):
        if a[i] != 0:
            if left == -1:
                left = i

            if i - left + 1 > best_len:
                best_len = i - left + 1
                best_l = left
                best_r = i

            if a[i] == 1:
                left = i

    for i in range(n):
        if a[i] == -1:
            a[i] = 0

    if best_l != -1:
        a[best_l] = 1
        a[best_r] = 1

    print(*a)
