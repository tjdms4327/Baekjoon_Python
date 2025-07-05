a,b=map(float, input().split())
c,d=map(float, input().split())

sums=[]
sums.append(a/c+b/d)
sums.append(c/d+a/b)
sums.append(d/b+c/a)
sums.append(b/a+d/c)
#print(sums)

print(sums.index(max(sums)))