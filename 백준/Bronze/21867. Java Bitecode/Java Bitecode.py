import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

result = s.replace('J','').replace('A','').replace('V','')
if len(result) == 0:
    print('nojava')
else:
    print(result)