import sys
input = sys.stdin.readline

n = int(input())
change = {}
for _ in range(n):
    a, b = input().strip().split()
    change[a] = b
    
m = int(input())
s = ''
for _ in range(m):
    x = input().strip()
    if x in change:
        s += change[x]
    else:
        s += x
print(s)