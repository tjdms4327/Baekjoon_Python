for _ in range(3):
    n=int(input())
    tot=0
    for _ in range(n):
        tot+=int(input())
    if tot==0:
        print(0)
    elif tot>0:
        print('+')
    else:
        print('-')