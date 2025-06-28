m=int(input())
n=int(input())
num=[]
for i in range(m,n+1):
    a=True
    for j in range(2,i):
        if i % j == 0:
            a=False
            break
    if a and i>1:
        num.append(i)

if num==[]:
    print(-1)
else:
    print(sum(num))
    print(min(num))