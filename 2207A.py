import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ones = [i for i, ch in enumerate(s) if ch == '1']
    if not ones:
        print(0, 0)
        continue
    mn = 0
    mx = 0
    start = ones[0]
    last = ones[0]

    for pos in ones[1:]:
        if pos - last <= 2:
            last = pos
        else:
            length = last - start + 1
            mx += length
            mn += length // 2 + 1

            start = pos
            last = pos

    length = last - start + 1
    mx += length
    mn += length // 2 + 1
    print(mn, mx)