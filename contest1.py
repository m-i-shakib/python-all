t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    excess = 0
    deficit = 0
    for ai, bi in zip(a, b):
        if ai > bi:
            excess += ai - bi
        elif ai < bi:
            deficit += bi - ai
    print(max(excess, deficit))