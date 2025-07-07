g,p,t=map(int, input().split())

option=g*p - (g+t*p)
if option==0:
    print(0)
elif option>0:
    print(2)
else: 
    print(1)