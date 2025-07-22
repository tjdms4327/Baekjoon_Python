n=int(input())
tot=0
for _ in range(n):
    k=list(input().strip())
    tot+=(k.count('A')*4 + k.count('K')*3 + k.count('Q')*2 + k.count('J'))
print(tot)