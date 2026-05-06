import sys
input=sys.stdin.readline
n=int(input())
f=list(map(int,input().split()))
for i in range(n):
    a=i+1
    b=f[i]
    c=f[b-1]
    if f[c-1]==a:
        print("YES")
        break
else:
    print("NO")
    