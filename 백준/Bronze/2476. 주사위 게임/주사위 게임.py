n=int(input())
m=[]
for i in range(n):
    a,b,c=map(int,input().split())
    if a==b==c:
        m.append(10000+1000*a)
    elif a==b or a==c:
        m.append(1000+100*a)
    elif b==c:
        m.append(1000+100*b)
    else:
        t=max(a,b,c)
        m.append(100*t)

print(max(m))