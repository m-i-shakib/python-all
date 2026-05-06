t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    s=(y+1)//2
    t=s*15
    u=y*4
    f=t-u
    if x>f:
        e=x-f
        s=s+(e+14)//15
    print(s)