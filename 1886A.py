t=int(input())
for _ in range(t):
    n=int(input())
    if n==6 or n==9 or n<6 :
        print("NO")
        continue
    if n==8:
        print("YES")
        print(1,2,5)
        continue

    print("YES")
    if n%3==0:
        print(1,4,n-5)
    elif n%3==1:
        print(1,2,n-3)
    else:
        print(2,4,n-6)
