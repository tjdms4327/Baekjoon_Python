a=[]
for i in range(5):
    b=list(map(int,input().split()))
    a.append(sum(b))

m=max(a)
print(a.index(m)+1,m)