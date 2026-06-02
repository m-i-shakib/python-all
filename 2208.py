from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    
    cnt = Counter()
    
    for _ in range(n):
        row = list(map(int, input().split()))
        cnt.update(row)
    
    max_freq = max(cnt.values())
    
    if max_freq <= n * (n - 1):
        print("YES")
    else:
        print("NO")