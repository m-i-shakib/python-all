import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    c=1
    a=0
    s=input().strip()
    for ch in s:
        d=int(ch)
        if d == 0:
            d = 10
        a+=abs(c-d)
        a+=1
        c=d
    print(a)