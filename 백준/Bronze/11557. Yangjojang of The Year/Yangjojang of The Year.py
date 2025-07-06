t=int(input())
for i in range(t):
    n=int(input())
    sc=[] ; ma=[]
    for i in range(n):
        a,b=input().split()
        sc.append(a) ; ma.append(int(b))
    k=ma.index(max(ma))
    print(sc[k])