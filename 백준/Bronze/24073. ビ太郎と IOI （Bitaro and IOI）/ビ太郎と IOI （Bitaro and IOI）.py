from itertools import groupby

n = int(input())
s = input().strip()

for ch in set(s):
    if ch not in 'IO':
        s = s.replace(ch, '')
        
s = ''.join(key for key, _ in groupby(s))
if 'IOI' in s:
    print('Yes')
else:
    print('No')