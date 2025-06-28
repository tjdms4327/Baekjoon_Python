for i in range(3):
    a=input().split()
    a0=a.count('0')
    if a0==1:
        print('A')
    elif a0==2:
        print('B')
    elif a0==3:
        print('C')
    elif a0==4:
        print('D')
    else:
        print('E')
