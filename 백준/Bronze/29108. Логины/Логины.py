import sys
input = sys.stdin.readline

s = input().strip()

if s[:2]=='io' and s[2:].isdigit():
    print('Correct')
else:
    print('Incorrect')