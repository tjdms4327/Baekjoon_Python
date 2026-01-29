import sys
input = sys.stdin.readline

n = list(map(int, input().strip()))

count = 0
while len(n) > 1:
    n = list(map(int, str(sum(n))))
    count += 1

print(count)
if n[0] % 3 == 0:
    print('YES')
else:
    print('NO')
