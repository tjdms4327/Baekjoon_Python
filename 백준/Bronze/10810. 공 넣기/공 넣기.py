n,m=map(int,input().split())

ball=[0 for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    for j in range(a-1,b):
        ball[j]=c

for k in range(n):
    print(ball[k], end=' ')