n=int(input())

a=100 ; b=100
for i in range(n):
    ac,bc=map(int,input().split())
    if ac>bc:
        b-=ac
    elif ac<bc:
        a-=bc
print(a)
print(b)