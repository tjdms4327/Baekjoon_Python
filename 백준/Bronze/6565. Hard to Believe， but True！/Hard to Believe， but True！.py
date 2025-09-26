# bronzeII_6565
import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    
    left, c = s.split('=')
    a, b = left.split('+')
    if int(a[::-1]) + int(b[::-1]) == int(c[::-1]):
        print('True')
    else:
        print('False')
    
    
    if s == '0+0=0': break