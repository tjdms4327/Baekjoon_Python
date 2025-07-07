n,m=map(int,input().split())

p=0
for _ in range(n):
    ox=input()
    if ox.count('O')>=ox.count('X'):
        p+=1

print(p)