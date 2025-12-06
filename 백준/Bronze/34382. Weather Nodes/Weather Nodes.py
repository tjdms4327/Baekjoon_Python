import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
    sys.exit()
temps = [float(input()) for _ in range(n)]

avg = sum(temps) / n
count = sum(1 for x in temps if abs(x-avg)>10)
print(count)