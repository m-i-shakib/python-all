t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = sum(a)

    if 2 * ones >= n:
        print("Bessie")
    else:
        print("Elsie")
