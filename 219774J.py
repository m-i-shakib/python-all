import sys
input=sys.stdin.readline
n=int(input())
a=list(map(int,input().split()))
m = min(a)
f=a.count(m)
if f%2==1:
    print("Lucky")
else:
    print("Unlucky")