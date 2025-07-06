y=list(map(int, input().split()))
y.sort()

if y[0]+y[1]==y[2] or (y[0]==y[1] or y[1]==y[2]):
    print('S')
else:
    print('N')