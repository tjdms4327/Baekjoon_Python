D,P =0,0

N=int(input())
for _ in range(N):
    win=input()
    if win=='D':
        D+=1
    else:
        P+=1
    if abs(D-P)==2:
        break
print(f'{D}:{P}')