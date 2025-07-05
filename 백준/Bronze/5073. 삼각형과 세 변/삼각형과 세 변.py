a,b,c=map(int,input().split())
while a+b+c != 0:
    if max([a,b,c])<sum([a,b,c])-max([a,b,c]):
        if a==b==c:
            print('Equilateral')
        elif a==b or b==c or c==a:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')
    a,b,c=map(int,input().split())