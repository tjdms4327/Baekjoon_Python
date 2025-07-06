n=int(input())

a=[]
for i in range(1,n+2):
    if i==1:
        a.append(0)
    elif i==2:
        a.append(1)
    else:
        a.append(a[-2]+a[-1])
print(a[-1])