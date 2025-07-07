max=0
for _ in range(7):
    name, n=input().split()
    n=int(n)

    if n>max:
        semina=name
        max=n
        
print(semina)
    