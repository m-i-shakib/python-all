t=int(input())
for _ in range(t):
    n,c=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(n):
        a[i]-=c
    for i in range(n//2):
        a[i]=max(a[i],0)
    print(sum(a))
