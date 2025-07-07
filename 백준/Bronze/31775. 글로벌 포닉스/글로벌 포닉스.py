s=list(input() for _ in range(3))
s.sort()

if s[0][0]=='k' and s[1][0]=='l' and s[2][0]=='p':
    print('GLOBAL')
else:
    print('PONIX')