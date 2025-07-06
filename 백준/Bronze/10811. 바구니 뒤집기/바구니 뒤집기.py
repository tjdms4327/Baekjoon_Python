n,m=map(int,input().split())
ball=[i for i in range(1,n+1)]

for j in range(m):
    a,b=map(int,input().split())
    ball2=ball[a-1:b]
    ball2.reverse()
    ball[a-1:b]=ball2
    #print(ball)

for k in range(n):
    print(ball[k], end=' ')