a=[]
for i in range(5):
    a.append(int(input()))
b=[a[0]+a[3],a[1]+a[3],a[2]+a[3],a[0]+a[4],a[1]+a[4],a[2]+a[4]]
print(min(b)-50)