ca,ba,pa=map(int,input().split())
cr,br,pr=map(int,input().split())

a=[cr-ca,br-ba,pr-pa]
n=0
for i in a:
    if i>0:
        n+=i
print(n)