def come_with(k,n):
    people=[i for i in range(1, n+1)]
    for _ in range(k):
        people=[sum(people[0:i]) for i in range(1, n+1)]
    return people[n-1]
    
t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    print(come_with(k,n))