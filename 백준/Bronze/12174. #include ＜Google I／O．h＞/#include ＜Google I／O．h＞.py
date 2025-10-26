# bronzeII_12174
import sys
input = sys.stdin.readline

mapping = {'I':'1', 'O':'0'}

t = int(input())
for case in range(1, t+1):
    b = int(input())
    s = input().strip()
    
    result = ''
    for i in range(0, b*8, 8):
        slice = s[i:i+8]
        real_slice = ''.join(mapping[ch] for ch in slice)
        
        result += chr(int(real_slice, 2))

    print(f'Case #{case}: {result}')