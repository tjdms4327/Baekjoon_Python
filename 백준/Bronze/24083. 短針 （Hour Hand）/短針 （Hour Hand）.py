a=int(input())
b=int(input())

time=(a+b)%12
if time==0:
    print(12)
else:
    print(time)