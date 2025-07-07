n=int(input())

s=1
for i in range(2,n+1):
    s*=i

w=s//60//60//24//7
print(w)