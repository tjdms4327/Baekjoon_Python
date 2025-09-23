# bronzeIII_21146.py
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
evaluations = sum(int(input()) for _ in range(k))

max_sum, min_sum = evaluations+3*(n-k), evaluations-3*(n-k)
print(min_sum/n, max_sum/n)