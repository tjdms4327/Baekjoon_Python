import sys
input = sys.stdin.readline

n = int(input())
yesterday = input().strip()
today = input().strip()


cnt = 0
for i in range(n):
    if 'C' == yesterday[i] == today[i]:
        cnt += 1
print(cnt)