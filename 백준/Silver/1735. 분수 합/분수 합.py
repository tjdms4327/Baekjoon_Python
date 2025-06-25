import math

a,b=map(int, input().split())
c,d=map(int, input().split())

up=a*d+c*b
down=b*d

gcd=math.gcd(up, down)
up//=gcd; down//=gcd
print(up, down)