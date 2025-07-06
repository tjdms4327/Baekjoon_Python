a=int(input())
b=int(input())
c=int(input())
d=int(input())
p=int(input())

x=p*a
y=b
if p>c:
    y+=((p-c)*d)
else:
    pass
m=[x,y]

print(min(m))