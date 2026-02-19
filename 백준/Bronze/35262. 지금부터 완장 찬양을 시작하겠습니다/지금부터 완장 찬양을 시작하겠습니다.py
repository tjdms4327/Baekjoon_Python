import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = input().strip().split('1')

if any(len(x)>=k for x in s):
    print(0)
else:
    print(1)