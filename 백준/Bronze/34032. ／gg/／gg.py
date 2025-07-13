import sys
input=sys.stdin.readline

n=int(input().strip())
s=input().strip()
if s.count('O')>=(n/2): print('Yes')
else: print('No')