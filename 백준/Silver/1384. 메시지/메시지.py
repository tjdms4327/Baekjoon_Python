import sys
input = sys.stdin.readline

case = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    case += 1
    
    names = []
    bad = []
    for i in range(n):
        name, *pn = input().strip().split()
        
        names.append(name)
        for j in range(n-1):
            if pn[j]=='N':
                bad.append(((i-j-1)%n, i))

    print(f'Group {case}')
    if bad:
        for i, j in bad:
            x, y = names[i], names[j]
            print(f'{x} was nasty about {y}')
    else:
        print('Nobody was nasty')
    print()