MOD= 998244353
t= int(input())
for _ in range(t):
    n,m,r,c=map (int,input().split())
    x=n*m-(n-r+1)*(m-c+1)
    print(pow(2,x,MOD))
