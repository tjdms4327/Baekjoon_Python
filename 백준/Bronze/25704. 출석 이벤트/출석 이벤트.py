n=int(input())
p=int(input())

num=0
if n>=5:
    num=max(num, 500)
if n>=10:
    num=max(num, p*0.1)
if n>=15:
    num=max(num, 2000)
if n>=20:
    num=max(num, p*.25)

p-=num
if p<=0:
    p=0
print(int(p))