x, y =map(int, input().split())

if (y//x)%2==0:
    print(y%x + x)
else:
    print(y%x)