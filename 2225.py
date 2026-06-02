t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    ans = "NO"

    for start in ['a', 'b']:
        target = ""
        
        for i in range(n):
            if i % 2 == 0:
                target += start
            else:
                if start == 'a':
                    target += 'b'
                else:
                    target += 'a'

        mismatch = []

        for i in range(n):
            if s[i] != target[i]:
                mismatch.append(i)

        if len(mismatch) == 0:
            ans = "YES"
            break

        first = mismatch[0]
        last = mismatch[-1]

        if last - first + 1 == len(mismatch):
            ans = "YES"
            break

    print(ans)