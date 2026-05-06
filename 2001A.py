import sys
def solve():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        freq = {}
        for v in a:
            freq[v] = freq.get(v, 0) + 1
        mx = max(freq.values())
        print(n - mx)
if __name__ == "__main__":
    solve()
