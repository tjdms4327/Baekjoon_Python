# bronzeII_2703.py
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    rule = list(input().strip())
    for i in range(len(s)):
        if s[i].isalpha():
            print(rule[ord(s[i]) - ord('A')], end='')
        else:
            print(s[i], end='')
    print()