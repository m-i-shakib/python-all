t = int (input())
b = "Yes"*20
for _ in range(t) :
    s = input().strip()
    if s in b:
        print("YES")
    else:
        print("NO")
