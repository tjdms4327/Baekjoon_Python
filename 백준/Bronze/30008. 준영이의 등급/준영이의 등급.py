n,k=map(int,input().split())
g=list(map(int,input().split()))

s=''
for i in g:
    p=(i*100)//n
    if p<=4:
        s+='1 '
    elif p<=11:
        s+='2 '
    elif p<=23:
        s+='3 '
    elif p<=40:
        s+='4 '
    elif p<=60:
        s+='5 '
    elif p<=77:
        s+='6 '
    elif p<=89:
        s+='7 '
    elif p<=96:
        s+='8 '
    else:
        s+='9 '
print(s)