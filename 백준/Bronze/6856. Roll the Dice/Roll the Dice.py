import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

cnt = sum(1 for i in range(1, m+1) if 1 <= 10-i <= n)

if cnt == 1:
    print(f'There is {cnt} way to get the sum 10.')
else:
    print(f'There are {cnt} ways to get the sum 10.')
