a=int(input())
x=int(input())
b=int(input())
y=int(input())
T=int(input())

if T>30: 
    a+=(T-30)*x*21
if T>45:
    b+=(T-45)*y*21
print(a,b)