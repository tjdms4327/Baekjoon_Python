a,b=map(int, input().split())
ma=int(input())
lista=list(map(int, input().split()))
listb=[]

tot=0
temp=1
for i in range(ma):
    tot+=lista[ma-i-1]*temp
    temp*=a
    
while (tot>0):
    listb.append(tot%b)
    tot//=b
    


lenb=len(listb)
for i in range(lenb):
    print(listb[lenb-i-1], end=' ' )