t = int(input())
for _ in range(t):
    n,k,m = map(int,input().split())
    if k>m:
        print("NO")
        continue
    print("YES")
    a=[]
    for i in range(n):
        if i%k==0:
            a.append(m-k+1)
        else:
            a.append(1)
    print(*a)
