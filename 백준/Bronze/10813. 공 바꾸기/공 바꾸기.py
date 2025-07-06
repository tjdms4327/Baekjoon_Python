n,m=map(int,input().split())
ball=[i for i in range(1,n+1)]

for j in range(m):
    a,b=map(int,input().split())
    ball[a-1],ball[b-1]=ball[b-1],ball[a-1]

for k in range(n):
    print(ball[k], end=' ')