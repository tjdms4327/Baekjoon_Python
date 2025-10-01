# bronzeIII_31052
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
x = [0] + list(map(int, input().split()))

for _ in range(q):
    num, a, b = map(int, input().split())
    if num == 1:
        x[a] = b
    else:
        print(abs(x[a] - x[b]))