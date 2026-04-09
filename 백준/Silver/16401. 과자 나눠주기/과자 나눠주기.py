import sys
input = sys.stdin.readline

m, n = map(int, input().split())
lengths = list(map(int, input().split()))


def can_split(k):
    cnt = 0
    for l in lengths:
        cnt += l//k
        
    return cnt >= m

left = 1
right = max(lengths)
answer = 0
while left <= right:
    mid = (left + right) // 2
    if can_split(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1
        
print(answer)