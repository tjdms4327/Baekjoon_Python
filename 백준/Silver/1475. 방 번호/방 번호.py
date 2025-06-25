a=input()
c=['0','1','2','3','4','5','6','7','8','9']
b=[] ; k=0
for i in c:
    d=a.count(i)
    if (i == '6') or (i =='9'):
        k+=d
    else:
        b.append(d)
if k%2==0:
    b.append(k//2)
else:
    b.append((k//2)+1)

print(max(b))