t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    odd_count = 0
    if x % 2 == 1:
        odd_count += 1
    if y % 2 == 1:
        odd_count += 1
    if odd_count <= 1:
        print("YES")
    else:
        print("NO")