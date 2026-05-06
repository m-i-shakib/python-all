s = input().strip()
q=0
qa=0
qaq=0
for ch in s:
    if ch == 'Q':
        qaq += qa
        q+=1
    elif ch =='A':
        qa += q
print(qaq)
