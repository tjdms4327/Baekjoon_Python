import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
len_s = len(s)

if len_s > n:
    print('Impossible')
else:
    print(sum(ord(i)-ord('a')+1 for i in s))