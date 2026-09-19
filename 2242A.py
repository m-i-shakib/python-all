t = int(input())

for _ in range(t):
    k = int(input())
    counts = list(map(int, input().split()))

    letters_with_two = sum(1 for count in counts if count >= 2)

    if max(counts) >= 3 or letters_with_two >= 2:
        print("YES")
    else:
        print("NO")