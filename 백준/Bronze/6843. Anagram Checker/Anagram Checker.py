# bronzeII_6843
import sys
input = sys.stdin.readline

s1 = list(input().strip().replace(' ', ''))
s2 = list(input().strip().replace(' ', ''))
s1.sort() ; s2.sort()

if s1 == s2:
    print('Is an anagram.')
else:
    print('Is not an anagram.')