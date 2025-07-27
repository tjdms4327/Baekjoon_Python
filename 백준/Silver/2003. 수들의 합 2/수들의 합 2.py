import sys
input=sys.stdin.readline

n, m=map(int, input().split())
A=list(map(int, input().split()))



start = 0
end = 0
current_sum = 0
count = 0

while True:
    if current_sum >= m:
        current_sum -= A[start]
        start += 1
    elif end == n:
        break
    else:
        current_sum += A[end]
        end += 1

    if current_sum == m:
        count += 1

print(count)