# bronzeII_5698
import sys
input = sys.stdin.readline

while True:  
    s = input().strip()
    if s == '*': break
    
    first_letter = [x[0].upper() for x in s.split()]
    if len(set(first_letter)) == 1:
        print('Y')
    else:
        print('N')