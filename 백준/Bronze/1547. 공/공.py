M=int(input())

ball=1
for _ in range(M):
    X,Y=map(int, input().split())
    if X==ball:
        ball=Y
    elif Y==ball:
        ball=X
print(ball)