import sys
input = sys.stdin.readline

s1 = list(map(len, input().strip().split('|')))
s2 = set(map(len, input().strip().split('|')))

print('Yes' if any(i in s2 for i in s1) else 'No')