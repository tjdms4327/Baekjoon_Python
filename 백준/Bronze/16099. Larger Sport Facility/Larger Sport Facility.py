for i in range(int(input())):
    lt,wt,le,we=map(int,input().split())
    t=lt*wt ; e=le*we
    if t>e:
        print('TelecomParisTech')
    elif t<e:
        print('Eurecom')
    else:
        print('Tie')