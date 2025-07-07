n=input()
a=list(map(int,input().split()))

h=0 ;s=0
for i in a:
    if i %2==0:
        h+=1
    else:
        s+=1
if h>s:
    print('Happy')
else:
    print('Sad')