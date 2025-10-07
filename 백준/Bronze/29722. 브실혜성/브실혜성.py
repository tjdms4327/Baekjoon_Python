# bronzeIII_29722
import sys
input = sys.stdin.readline

y, m, d = map(int, input().split("-"))
n = int(input())
 
d += n
m += (d - 1) // 30
d = (d - 1) % 30 + 1
y += (m - 1) // 12
m = (m - 1) % 12 + 1
print(f'{y:04d}-{m:02d}-{d:02d}')