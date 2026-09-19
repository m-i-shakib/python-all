t=int (input())
for _ in range (t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=int(input())-1
    x=a[p]
    l=int(a[0]!=x)
    for i in range(1,p+1):
        l+=a[i]!= a[i-1]
    r=int(a[-1]!=x)
    for i in range(p+1,n):
        r+=a[i]!=a[i-1]
    print(max(l,r))
