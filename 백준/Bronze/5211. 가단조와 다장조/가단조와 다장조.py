# bronzeII_5211
import sys
input = sys.stdin.readline

s = list(input().strip().split('|'))
count_c, count_a = 0, 0
for i in s:
    if i[0] in 'CFG':
        count_c += 1
    elif i[0] in 'ADE':
        count_a += 1
            
if count_c > count_a:
    print('C-major')
elif count_c < count_a:
    print('A-minor')
else:
    last_note = s[-1][-1]
    if last_note in 'CFG':
        print('C-major')
    else:
        print('A-minor')