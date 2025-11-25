import sys
input = sys.stdin.readline

n = int(input())

i = 1
while n > i:
    n -= i
    i += 1
x1, x2 = 1, i
for _ in range(n-1):
    x1 += 1
    x2 -= 1
print(x2, x1)