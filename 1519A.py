import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    l=max(a,b)
    s=min(a,b)
    if l<=s *(c+1):
        print("YES")
    else:
        print("NO")
        