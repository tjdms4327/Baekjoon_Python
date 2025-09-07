import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

min_len = N + 1 
sum = 0 
start = 0

for end in range(N):
    sum += numbers[end]
    while sum >= S:
        min_len = min(min_len, end - start + 1)
        sum -= numbers[start]
        start += 1

print(0 if min_len == N + 1 else min_len)