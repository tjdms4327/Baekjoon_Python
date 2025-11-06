# bronzeII_25905
import sys
input = sys.stdin.readline

P = [float(input()) for _ in range(10)]
P.sort()

ans = 1
for i in range(1, 10):
    ans *= P[i] / i
print(ans * 1e9)