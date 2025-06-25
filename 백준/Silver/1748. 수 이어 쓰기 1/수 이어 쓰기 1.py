n=int(input())

tot=0
d=len(str(n))
for i in range(d):
    tot+=9*(10**(i-1))*i
tot+=(n-(10**(d-1))+1)*d
print(int(tot))