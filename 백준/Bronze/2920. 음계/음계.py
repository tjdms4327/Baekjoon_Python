a=list(map(int,input().split()))

b=0 ;c=0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        b+=0 ; c+=1
    elif a[i]<a[i+1]:
        b+=1 ; c+=1
    else:
        pass
if b==0:
    print('descending')
elif b==c:
    print('ascending')
else:
    print('mixed')