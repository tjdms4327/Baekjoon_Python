# bronzeII_32621
import sys
input = sys.stdin.readline

s = input().strip()

if s == '+':
    print('No Money')
else:
    s_lst = s.split('+')
    
    if len(s_lst) != 2:
        print('No Money')
    else:
        a, b = s_lst
        if a == b and a.isdigit() and not a.startswith('0') and int(a) > 0:
            print('CUTE')
        else:
            print('No Money')
