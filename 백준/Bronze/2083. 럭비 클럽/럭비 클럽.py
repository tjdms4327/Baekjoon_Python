while True:
    a=input().split()
    if a == ['#','0','0']:
        break
    else:
        a[1]=int(a[1]) ; a[2]=int(a[2])
        if a[1]>17 or a[2]>=80:
            print(a[0],'Senior')
        else:
            print(a[0],'Junior')