import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    n= int(input())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    po=[0]*(n+1)
    for i in range(n):
        po[p[i]]=i
    lst=-1
    o= True
    for x in a:
        if po[x]< lst:
            o=False
            break
        lst=po[x]
    print("YES" if o else "NO")
