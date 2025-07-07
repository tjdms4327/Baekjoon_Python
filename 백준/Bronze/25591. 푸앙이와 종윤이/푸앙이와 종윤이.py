x, y =map(int, input().split())

a, b=100-x, 100-y
c, d=100-(a+b), a*b
q, r=d//100, d%100
print(a,b,c,d,q,r)

if q!=0:
    print(c+q, r)
else:
    print(c,d)