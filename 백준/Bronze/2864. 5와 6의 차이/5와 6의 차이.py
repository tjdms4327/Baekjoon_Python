a,b=input().split()

if '6' in a:a=a.replace('6', '5')
if '6' in b: b=b.replace('6', '5')
print(int(a)+int(b), end=' ')

if '5' in a: a=a.replace('5', '6')
if '5' in b: b=b.replace('5', '6')
print(int(a)+int(b))