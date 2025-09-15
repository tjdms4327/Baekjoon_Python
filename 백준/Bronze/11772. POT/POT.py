import sys
input = sys.stdin.readline

n = int(input())
sum = 0
for _ in range(n):
    p = input().strip()
    if len(p) == 1:
        sum += int(p)
    else:
        sum += int(p[:-1]) ** int(p[-1])
print(sum)