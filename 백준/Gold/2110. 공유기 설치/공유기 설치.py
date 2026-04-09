import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = [int(input()) for _ in range(n)]
houses.sort()



left = 1 # 최소 거리
right = houses[-1] - houses[0] # 최대 거리

def can_install(distance):
    count = 1 # 첫 집에 설치
    last = houses[0] # 마지막 설치 위치
    
    for i in range(1, n):
        if houses[i]-last >= distance:
            count += 1
            last = houses[i]
    return count >= c 

answer = 0
while left <= right:
    mid = (left+right) // 2
    
    if can_install(mid):
        left = mid+1
        answer = mid
    else:
        right = mid-1
        
print(answer)