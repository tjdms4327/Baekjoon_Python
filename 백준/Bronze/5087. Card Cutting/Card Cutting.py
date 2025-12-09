import sys
input = sys.stdin.readline

while True:
    lst = list(input().strip().split())
    if lst == ['#']:
        break
    
    c, t = 0, 0
    for x in lst[:-1]:
        if x == 'A':
            c += 1
        else:
            x = int(x)
            if x%2==1:
                c += 1
            else:
                t += 1
                
    if c > t:
        print('Cheryl')
    elif c < t:
        print('Tania')
    else:
        print('Draw')