t = int(input())
for _ in range(t):
    k = int(input())
    a1,b1=map(int,input().split())
    a2,b2=map(int,input().split())
    a=a1+a2
    b=b1+b2
    if a-b>=k:
        print("NO")
    else:
        print("YES")
