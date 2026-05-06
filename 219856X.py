import sys
input = sys.stdin.readline
s = input()
n = len(s)
if n == 1:
    print(s)
else:
    small = s
    for i in range(1, n):
        p1 = s[:i]
        p2 = s[i:]
        p1 = ''.join(sorted(p1))
        p2 = ''.join(sorted(p2))
        string = p1 + p2
        if string < small:
            small = string
    print(small)