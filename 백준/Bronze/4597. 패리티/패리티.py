while True:
    a=input().strip()
    if a=='#': break

    parity=a[-1]
    num=a[:-1]
    one=num.count('1')
    if (parity=='e'and one%2==1):
            print(num+'1')
    elif parity=='o' and one%2==0:
            print(num+'1')
    else:
        print(num+'0')