a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
time=0

if a<0:
    time+=c*(-a)
    a=0
if a==0:
    time+=d
if a>=0 and a<b:
    time+=(e*(b-a))

print(time)