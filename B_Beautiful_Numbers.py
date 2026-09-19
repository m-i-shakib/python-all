t = int(input())
for _ in range(t):
    x=input().strip()
    s=0
    a=[]
    for i in range(len(x)):
        d=int(x[i])
        s+=d
        if i==0:
            a.append(d-1)
        else:
            a.append(d)
    if s<=9:
        print(0)
        continue
    a.sort(reverse=True)
    n=s-9
    ans=0
    for v in a:
        n-=v
        ans += 1
        if n<=0:
            break
    print(ans)
