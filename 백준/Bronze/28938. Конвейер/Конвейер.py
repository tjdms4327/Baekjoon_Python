n=input()
a=list(map(int,input().split()))
b=sum(a)
if b>0:
    print('Right')
elif b==0:
    print('Stay')
else:
    print('Left')