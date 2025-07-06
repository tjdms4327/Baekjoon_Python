t=int(input())
for _ in range(t):
    n=int(input())
    tot=0
    for i in range(1,n+1,2):
        tot+=i
    print(tot)