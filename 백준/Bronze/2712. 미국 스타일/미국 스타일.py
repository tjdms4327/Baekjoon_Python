def change(n,k):
    n=float(n)
    if k=='kg':
        return (n*2.2046),' lb'
    elif k=='lb':
        return (n*0.4536),' kg'
    elif k=='l':
        return (n*0.2642),' g'
    else:
        return (n*3.7854),' l'

t=int(input())
for _ in range(t):
    n,k=input().split()
    changed,k=change(n,k)
    print(f'{changed:.4f}{k}')