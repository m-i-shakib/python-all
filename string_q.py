import sys
input=sys.stdin.readline
s = input()
a = s.split()
r = []
for w in a:
    r.append(w[::-1])
print(" ".join(r))
