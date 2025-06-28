m=[0]
for i in range(10):
    a,b=map(int,input().split())
    c=b-a
    m.append(m[-1]+c)
print(max(m))