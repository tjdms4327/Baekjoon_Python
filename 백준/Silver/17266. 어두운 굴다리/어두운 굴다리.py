import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
X = list(map(int, input().split()))


def can_cover(h):
    if X[0] - h > 0: # 시작점
        return False
    
    last = 0
    for i in range(1, m):
        if X[i]-X[i-1] > 2*h:
            return False
    
    if X[-1]+h < n: # 끝점
        return False
    
    return True

left = 1
right = n
while left <= right:
    mid = (left+right) // 2
    
    if can_cover(mid):
        right = mid - 1
    else:
        left = mid + 1

print(left)