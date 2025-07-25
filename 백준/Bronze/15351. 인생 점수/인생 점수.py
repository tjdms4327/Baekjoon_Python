t=int(input())
for _ in range(t):
    s=input()
    
    life=0
    for i in s:
        if i.isalpha():
            life+=ord(i)-ord('A')+1
        
    if life==100:
        print('PERFECT LIFE')
    else: 
        print(life)