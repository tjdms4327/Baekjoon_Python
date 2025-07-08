import sys
input=sys.stdin.readline

s=input().strip() 
# D2와 d2 모두 고려하는 것보다 모두 대문자처리하는게 쉬움
if 'D2' in s.upper():
    print('D2')
else: print('unrated')