n=int(input())
a=set(list(map(int, input().split())))
 
m=int(input())
num=list(map(int, input().split()))
for i in num:
    if i in a:
        print(1)
    else:
        print(0)