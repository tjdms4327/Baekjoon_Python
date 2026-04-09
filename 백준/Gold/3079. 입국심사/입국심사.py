import sys
input = sys.stdin.readline

n, m = map(int, input().split())
T = [int(input()) for _ in range(n)]


def possible(time):
    total = 0
    for t in T:
        total += time // t
    return total >= m

left = 1
right = max(T) * m # 제일 느린 곳에서 모두 처리
answer = right
while left <= right:
    mid = (left + right) // 2
    if possible(mid):
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
        
print(answer)