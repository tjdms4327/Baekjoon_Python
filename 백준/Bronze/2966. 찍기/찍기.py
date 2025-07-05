def find_winner(n, answer):
    palyers={'Adrian':0, 'Bruno':0, 'Goran':0}
    for i in range(n):
        if (i%3==0 and answer[i]=='A') or (i%3==1 and answer[i]=='B') or (i%3==2 and answer[i]=='C'):
            palyers['Adrian']+=1
        if (i%2==0 and answer[i]=='B') or (i%4==1 and answer[i]=='A') or (i%4==3 and answer[i]=='C'):
            palyers['Bruno']+=1
        if  ((i%6==0 or i%6==1) and answer[i]=='C') or ((i%6==2 or i%6==3) and answer[i]=='A') or ((i%6==4 or i%6==5) and answer[i]=='B'):
            palyers['Goran']+=1

    max_score = max(palyers.values())
    winners = [key for key, val in palyers.items() if val == max_score]
    print(max_score)
    print(*winners, sep='\n')

        
n=int(input())
answer=input()
find_winner(n, answer)
