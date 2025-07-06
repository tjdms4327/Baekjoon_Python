win=input()


score=[11,11]
winner=None
for i in range(0,len(win)-1,2):
    if win[i]=='A':
        score[0]-=int(win[i+1])
    else:
        score[1]-=int(win[i+1])
    
    if score[0]==1 and score[1]==1:
        score[0]+=2
        score[1]+=2
        
    if score[0]==0:
        winner='A'
        break
    if score[1]==0:
        winner='B'
        break

if winner:
    print(winner)
else:
    if score[0]<score[1]:
        print('A')
    else:
        print('B')







