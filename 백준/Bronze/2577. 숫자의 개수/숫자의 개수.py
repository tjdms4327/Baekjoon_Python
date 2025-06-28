a=[]
for i in range(3):
    a.append(int(input()))

b=str(a[0]*a[1]*a[2])
for i in range(10):
    print(b.count(str(i)))