start=list(map(int, input().split()))
last=list(map(int, input().split()))

score=0
comeback_loss='No'
for i in range(9):
    score+=start[i]
    if score>0:
        comeback_loss='Yes'
        break
    score-=last[i]
    if score>0:
        comeback_loss='Yes'
        break
print(comeback_loss)