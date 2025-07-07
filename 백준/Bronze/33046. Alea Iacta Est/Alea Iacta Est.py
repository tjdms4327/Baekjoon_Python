a,b=map(int, input().split())
c,d=map(int, input().split())

player2=((1-1)+(a+b))%4
player3=((player2-1)+(c+d))%4
print(player3 if player3!=0 else 4)