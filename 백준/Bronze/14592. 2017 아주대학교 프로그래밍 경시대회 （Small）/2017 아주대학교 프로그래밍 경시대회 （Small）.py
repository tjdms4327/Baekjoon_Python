N=int(input())

winner,S,C,L=0,0,0,0
for i in range(1,N+1):
    Si,Ci,Li=map(int, input().split())
    if Si>S:
        winner=i
        S,C,L=Si,Ci,Li
    elif Si==S:
        if Ci<C:
            winner=i
            S,C,L=Si,Ci,Li
        elif Ci==C:
            if Li<L:
                winner=i
                S,C,L=Si,Ci,Li
print(winner)