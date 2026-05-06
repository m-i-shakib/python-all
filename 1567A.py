import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    t=""
    for ch in s:
        if ch == "U":
            t+="D"
        elif ch == "D":
            t+="U"
        else:
            t+=ch
    print(t)