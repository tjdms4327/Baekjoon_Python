import sys
input = sys.stdin.readline

n, m = map(int, input().split())
road = list(map(int, input().split()))

# 초기 덩어리
cnt = 0
for i in range(n):
    if road[i] == 1 and (i == 0 or road[i-1] == 0):
        cnt += 1

for _ in range(m):
    q = input().strip().split()
    
    if q[0] == '0':
        print(cnt)
    else:
        x = int(q[1]) - 1
        if road[x] == 0:
            left = (x > 0 and road[x-1] == 1)
            right = (x < n-1 and road[x+1] == 1)
            
            if not left and not right:
                cnt += 1
            elif left and right:
                cnt -= 1
            
            road[x] = 1
