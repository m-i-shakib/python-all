t = int(input())
for _ in range(t):
    n,x,y,z=map(int,input().split())
    if n<=3:
        print(1)
    else:
        d=abs(x-y)
        d=min(d,n-d)
        print(d+z)
