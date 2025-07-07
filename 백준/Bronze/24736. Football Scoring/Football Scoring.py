a=[]
for i in range(2):
    t,f,s,p,c=map(int,input().split())
    a.append(t*6+f*3+s*2+p*1+c*2)
print(*a, end=' ')
