import sys
input = sys.stdin.readline

n = int(input().strip())
count = 0

count += min(n, 9) + 1
for d in range(1, 10):
    num = d
    while True:
        num = num * 10 + d
        if num > n:
            break
        count += 1

print(count)
