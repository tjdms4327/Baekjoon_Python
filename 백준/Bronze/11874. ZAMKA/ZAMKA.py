# bronzeIII_11874
import sys
input = sys.stdin.readline

l = int(input())
d = int(input())
x = int(input())

for n in range(l, d+1):
    if sum(map(int, str(n))) == x:
        print(n)
        break
for m in range(d, l-1, -1):
    if sum(map(int, str(m))) == x:
        print(m)
        break