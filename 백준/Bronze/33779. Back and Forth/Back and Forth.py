import sys
input = sys.stdin.readline

s = input().strip()
if s == s[::-1]:
    print('beep')
else:
    print('boop')