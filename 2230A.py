t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    three_individual = 3 * a

    if three_individual <= b:
        print(n * a)
    else:
        full_groups = n // 3
        remaining = n % 3

        cost = full_groups * b

        cost += min(remaining * a, b)

        print(cost)