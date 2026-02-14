import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

print(2*(max(nums)-min(nums)))