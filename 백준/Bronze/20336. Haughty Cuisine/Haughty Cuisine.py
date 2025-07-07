import random

menu=[]

n=int(input())
for _ in range(n):
    num, *name=input().split()
    menu.append(name)
    
random_menu=random.choice(menu)
print(len(random_menu))
print(*random_menu, sep='\n')