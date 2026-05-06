import sys
input=sys.stdin.readline
q = int(input())
s = input()
key = "PgEfTYaWGHjDAmxQqFLRpCJBownyUKZXkbvzIdshurMilNSVOtec#@_!=.+-*/"
orig = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
r = ""
for ch in s:
    if q == 1: 
        index = orig.index(ch)
        r += key[index]
    else: 
        index = key.index(ch)
        r += orig[index]
print(r)