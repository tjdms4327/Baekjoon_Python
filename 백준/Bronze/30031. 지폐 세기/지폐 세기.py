m=0
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==136:
        m+=1000
    elif a==142:
        m+=5000
    elif a==148:
        m+=10000
    else:
        m+=50000
print(m)