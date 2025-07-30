x=int(input())
n=int(input())

cnt=0
while x<n:
    r=x%3
    if r==0: x+=1
    elif r==1: x*=2
    else: x*=3
    cnt+=1
print(cnt)