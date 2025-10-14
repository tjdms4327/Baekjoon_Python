# bronzeII_1773
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

time = set()
for _ in range(n):
    period = int(input())
    time.update(range(period, c+1, period))
print(len(time))