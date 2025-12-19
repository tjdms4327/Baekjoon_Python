import sys
input = sys.stdin.readline

for _ in range(int(input())):
    line = list(input().strip().split())
    
    result = []
    for x in line:
        m = x.count('M')
        o = x.count('O')
        
        hex_str = format(m, 'x') + format(o, 'x')
        result.append(chr(int(hex_str, 16)))
    
    print(''.join(result))