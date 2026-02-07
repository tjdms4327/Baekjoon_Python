import sys
input = sys.stdin.readline

n, m = map(int, input().split())
if n == 0:
    print(0)
    sys.exit()
books = list(map(int, input().split()))

box = 0
weight = 0
for x in books:
    if weight+x <= m:
        weight += x
    else:
        box += 1
        weight = x
        
if weight > 0:
    box += 1
    
print(box)