# bronzeI_9946
import sys
input = sys.stdin.readline

case = 0
while True:  
    s1 = input().strip()
    if s1 == 'END':
        input()
        sys.exit()
    
    case += 1
    s1 = sorted(list(s1))
    s2 = sorted(list(input().strip()))
    if s1 == s2:
        print(f'Case {case}: same')
    else:
        print(f'Case {case}: different')