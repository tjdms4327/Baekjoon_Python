N, A=map(int,input().split())
recipt=list(map(int,input().split()))

ticket=0
rlen=len(recipt)
for i in range(rlen):
    if recipt[i]>=A:
        ticket+=recipt[i]//A
print(ticket)