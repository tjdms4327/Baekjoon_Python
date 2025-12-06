import sys
input = sys.stdin.readline

n = int(input())

for m in range(60, 0, -1):
    if (n + 60*m) % 3600 < 60:
        print(m)
        break