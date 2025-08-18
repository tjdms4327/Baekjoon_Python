import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]


ans = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
for i in range(n):
    if nums[i] == ans:
        print(i+1)