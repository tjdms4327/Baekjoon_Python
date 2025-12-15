import sys
input = sys.stdin.readline

while True:   
    s = input().strip()
    if s == 'quit!':
        break
    
    if (len(s)>4) and (s[-2:]=='or') and (s[-3] not in 'aeiouy'):
        print(s[:-2]+'our')
    else:
        print(s)