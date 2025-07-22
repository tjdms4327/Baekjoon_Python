n=int(input())

fee=0
cand=[]
for _ in range(n):
    d, c=input().split()
    if d=='jinju':
        fee=int(c)
    else:
        cand.append(int(c))
print(fee)
print(sum(i>fee for i in cand))