from math import gcd
def lcm(x,y):
    return x*y//gcd(x,y)
t=int(input())
for _ in range(t):
    a,b,c,m=map(int,input().split())
    ab=lcm(a,b)
    ac=lcm(a,c)
    bc=lcm(b,c)
    abc=lcm(ab,c)
    A=m//a
    B=m//b
    C=m//c
    AB=m// ab
    AC=m//ac
    BC=m//bc
    ABC=m//abc
    al=6*A-3*AB-3*AC+2*ABC
    bo=6*B-3*AB-3*BC+2*ABC
    ca=6*C-3*AC-3*BC+2*ABC
    print(al,bo,ca)
