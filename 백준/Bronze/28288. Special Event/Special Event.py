import sys
input = sys.stdin.readline

n = int(input())
attendable = [input().strip() for _ in range(n)]

days = [col.count('Y') for col in zip(*attendable)]
days = [-1] + days

max_attend = max(days)
print(','.join(str(i) for i, val in enumerate(days) if val == max_attend))