import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0] + list(map(int, input().split()))

if A[m] == m:
    print(0)
    sys.exit()
    
cur = m
count = 0
while True:
    count += 1
    cur = A[cur]
    if cur == m:
        break

print(count)