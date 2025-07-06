n,m=map(int,input().split())
a=[];x=0
for i in range(n):
    a.append(input())
for j in range(m):
    if input() in a:
        x+=1
print(x)