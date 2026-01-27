import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
for i in range(1, 1+t):
    s = input().strip().lower()
    count = Counter(s)
    
    min_v = []
    for idx, val in count.items():
        if ord('a') <= ord(idx) <= ord('z'):
            min_v.append(val)
    
    print(f'Case {i}: ', end='')
    if len(min_v) < 26:
        print('Not a pangram')
    else:
        Min = min(min_v)
        if Min == 1:
            print('Pangram!')
        elif Min == 2:
            print('Double pangram!!')
        else:
            print('Triple pangram!!!')