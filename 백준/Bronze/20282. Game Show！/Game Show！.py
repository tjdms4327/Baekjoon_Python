import sys
input = sys.stdin.readline

c = int(input())
V = [int(input()) for _ in range(c)]

credit = [100]
for v in V:
    credit.append(credit[-1] + v)
print(max(credit))