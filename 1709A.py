import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a,b,c=map(int,input().split())
    d=[0,a,b,c]
    if d[n]!=0 and d[d[n]]!=0:
        print("YES")
    else:
        print("NO")
        