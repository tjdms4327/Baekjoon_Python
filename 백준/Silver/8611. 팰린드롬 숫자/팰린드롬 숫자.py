import sys
input = sys.stdin.readline


n = int(input())

result = []
for b in range(2, 11):
    temp = []
    x = n
    while x >= b:
        temp.append(str(x%b))
        x //= b
    temp.append(str(x%b))
        
    bx = ''.join(temp[::-1])
    if bx == bx[::-1]:
        result.append((b, bx))

if not result:
    print('NIE')
else:
    for b, val in result:
        print(b, val)