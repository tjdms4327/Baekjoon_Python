# bronzeIII_31669
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
patrol = [input().strip() for _ in range(n)]

t = 1
for time in zip(*patrol):
    if all(i == 'X' for i in time):
        print(t)
        exit()
    t += 1
print('ESCAPE FAILED')