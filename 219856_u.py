import sys
s = sys.stdin.readline().strip().lower()
c = {'e': 0, 'g': 0, 'y': 0, 'p': 0, 't': 0}
for ch in s:
    if ch in c:
        c[ch] += 1
print(min(c.values()))
