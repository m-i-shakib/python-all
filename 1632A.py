t = int(input())
for _ in range(t):
    n= int(input())
    s= input().strip()
    if n==1:
        print("YES")
    elif n ==2:
        if '0' in s and '1' in s:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")