n=int(input())

d=[]
for i in range(n):
    a,b=map(int,input().split())
    if b-a>=0:
        d.append(b)
if len(d)==0:
    print(-1)
else:
    print(min(d))