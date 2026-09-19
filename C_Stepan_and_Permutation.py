from math import gcd

t = int(input())
for _ in range(t):
    n,x,y=map(int,input().split())
    p=list(map(int,input().split()))
    g=gcd(x,y)
    o=True
    for i in range(n):
        if p[i]%g!=(i+1)%g:
            o=False
            break
    print("YES" if o else "NO")
