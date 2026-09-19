t=int(input())
for _ in range(t):
    n,k =map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=[]
    for l in range(k,0,-1):
        for i in range(n):
            if b[i]==l:
                x=l
                for j in range(l,k+1):
                    ans.append(i+1)

    print(len(ans))
    print(*ans)
