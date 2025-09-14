import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
discount = ((m + 1) * s * (100 - n)) // 100
plus_one = m * s

print(min(discount, plus_one))