# bronzeI_2999
import sys
input = sys.stdin.readline

s = input().strip()
n = len(s)

for i in range(int(n**0.5), 0,-1):
    if n % i == 0:
        r = min(i, n//i)
        c = max(i, n//i)
        break

matrix = []
for i in range(0, n, r):
    matrix.append(s[i:i+r])

for col in zip(*matrix):
    print(''.join(col), end='')
