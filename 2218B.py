t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    
    total = sum(a)
    mx = max(a)
    
    ans = 2 * mx - total
    print(ans)