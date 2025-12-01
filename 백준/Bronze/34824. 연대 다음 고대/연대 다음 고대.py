import sys
input = sys.stdin.readline

n = int(input())

names = [input().strip() for _ in range(n)]
yonsei = names.index('yonsei')
korea = names.index('korea')
if yonsei < korea:
    print('Yonsei Won!')
else:
    print('Yonsei Lost...')