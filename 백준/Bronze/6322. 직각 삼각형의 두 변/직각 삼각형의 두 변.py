i=0
while True:
    a, b, c=map(int,input().split())
    if a==0 and b==0 and c==0: break

    i+=1
    print(f'Triangle #{i}')
    if c==-1:
        c=(a**2+b**2)**0.5
        if c<=a or c<=b:
            print(f'Impossible.\n')
        else: 
            print(f'c = {c:.3f}\n')
    elif a==-1:
        if c<=b: print(f'Impossible.\n')
        else:
            a=(c**2-b**2)**0.5
            if a>=c: 
                print(f'Impossible.\n')
            else: 
                print(f'a = {a:.3f}\n')
    else: # b=-1
        if c<=a: print(f'Impossible.\n')
        else:
            b=(c**2-a**2)**0.5
            if b>=c: 
                print(f'Impossible.\n')
            else: 
                print(f'b = {b:.3f}\n')
    #print(a, b, c)