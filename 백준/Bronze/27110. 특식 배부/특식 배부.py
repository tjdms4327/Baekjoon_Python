N=int(input())
num=map(int,input().split())

result=0
for i in num:
    if i<=N:
        result+=i
    else:
        result+=N
print(result)