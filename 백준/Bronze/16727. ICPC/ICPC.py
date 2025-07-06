P1, E1=map(int, input().split())
E2, P2=map(int, input().split())

P,E=P1+P2, E1+E2
if P>E:
    print('Persepolis')
elif P<E:
    print('Esteghlal')
else:
    if P2>E1:
        print('Persepolis')
    elif P2<E1:
        print('Esteghlal')
    else:
        print('Penalty')