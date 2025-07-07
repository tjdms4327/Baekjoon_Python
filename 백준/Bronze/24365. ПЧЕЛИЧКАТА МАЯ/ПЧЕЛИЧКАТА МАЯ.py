import sys
input=sys.stdin.readline

a,b,c=map(int, input().split())

avg=(a+b+c)//3 
if b==avg:
    print((avg-a)*2)
elif b>avg:
    print((c-avg)*2+(b-avg))
else:
    print((avg-b)+(avg-a)*2)