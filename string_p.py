import sys
input=sys.stdin.readline
s = input()
for ch in "!.,?":
    s = s.replace(ch, " ")
words = s.split()
print(len(words))
