m,s,g=map(float, input().split())
a,b=map(float, input().split())
l,r=map(float, input().split())

right=(m/s)*(r/b)
left=(m/g)*(l/a)
if right<left:
    print('latmask')
else:
    print('friskus')