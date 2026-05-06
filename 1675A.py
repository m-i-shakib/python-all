t=int(input())
for _ in range(t):
    a,b,u,x,y = map(int,input().split())
    d=max(0,x-a)
    c=max(0,y-b)
    if d+c<=u:
        print("YES")
    else:
        print("NO")