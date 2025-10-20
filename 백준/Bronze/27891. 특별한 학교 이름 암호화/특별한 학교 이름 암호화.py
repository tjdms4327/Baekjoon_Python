s = input().strip()

diff01 = (ord(s[1]) - ord(s[0])) % 26
if diff01 == 1:
    diff12 = (ord(s[2]) - ord(s[1])) % 26
    if diff12 == 3:
        print('NLCS')
    else:
        print('SJA')
elif diff01 == 16:
    print('BHA')
else:
    print('KIS')
    