import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []
    for _ in range(t):
        n = int(next(it))
        a = [int(next(it)) for _ in range(n)]
        seen = set()
        ok = False
        for v in a:
            if v in seen:
                ok = True
                break
            seen.add(v)
        out_lines.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
