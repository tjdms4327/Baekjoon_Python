import sys
input = sys.stdin.readline

s = input().strip().split('()')

if s[0] == s[1]:
    print('correct')
else:
    print('fix')