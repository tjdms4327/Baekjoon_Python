import sys
input = sys.stdin.readline

b, n, m = map(int, input().split())
item = {}
for _ in range(n):
    i, p = input().strip().split()
    item[i] = int(p)

purchase = set(input().strip() for _ in range(m))    
for x in purchase:
    b -= item[x]
    
if b >= 0:
    print('acceptable')
else:
    print('unacceptable')