import sys
input = sys.stdin.readline

n = int(input())
count = [int(input()) for _ in range(n)]

avg = sum(count) // n
result = [num-avg for num in count if num > avg]
print(sum(result))