fibbo=[0,1]

n=int(input())
for _ in range(1,n):
    fibbo.append(fibbo[-1]+fibbo[-2])
print(fibbo[-1])