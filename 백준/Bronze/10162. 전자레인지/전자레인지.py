t=int(input())

a=300
b=60
c=10

r=''
if t%10 !=0:
    print(-1)
else:
    m5=t//a
    m1=(t-m5*300)//60
    s10=(t-m5*300-m1*60)//10
    print(m5,m1,s10)