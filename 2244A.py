import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    max_length = 0
    current_length = 0
    for ch in s:
        if ch == '#':
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    answer = (max_length + 1) // 2
    print(answer)