import sys
input = sys.stdin.readline

n = int(input())
X = list(map(int, input().split()))

if any(X[i]-X[i-1]<2 for i in range(1, n)):
    print(-1)
    sys.exit()

move = 0
cur = 0
for x in X:
    while x-cur >= 3:
        cur += 2
        move += 1
    if x-cur ==2:
        cur += 1
        move += 1
    
    # 장애물 점프
    cur += 2 
    move += 1 

print(move)