import sys
input=sys.stdin.readline
s=input()
c=0
start=0
a=[]
for i in range(len(s)):
    if s[i]=='R':
        c+=1
    else:
        c-=1
    if c==0:
        a.append(s[start:i+1])
        start=i+1
print(len(a))
for x in a:
    print(x)