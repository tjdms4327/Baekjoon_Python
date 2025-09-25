# bronzeII_4575
import sys
input = sys.stdin.readline

while True:
    S = input().strip()
    if S == 'END': break
    
    s = S.replace(' ', '')
    if len(s) == len(set(s)):
        print(S)