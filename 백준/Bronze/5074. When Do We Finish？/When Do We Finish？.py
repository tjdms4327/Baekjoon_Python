while True:
    a, b=input().split()
    if a=='00:00' and b=='00:00': break
    
    a=list(a.split(':')) ; b=list(b.split(':'))
    minute=int(a[1])+int(b[1])
    hour=int(a[0])+int(b[0])

    if minute>=60:
        hour+=minute//60; minute%=60
    if hour>=24:
        day=hour//24 ; hour%=24
        print(f'{hour:02d}:{minute:02d} +{day}')
    else: print(f'{hour:02d}:{minute:02d}')