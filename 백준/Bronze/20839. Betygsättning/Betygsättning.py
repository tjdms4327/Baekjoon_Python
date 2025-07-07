x,y,z=map(int, input().split())
x_,y_,z_=map(int, input().split())

if z==z_:
    if y==y_:
        if x==x_:
            print('A')
        elif x/2<=x_:
            print('B')
        else:
            print('C')
    elif y/2<=y_:
        print('D')
    else:
        print('E')