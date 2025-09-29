# bronzeIV_34543
import sys
input = sys.stdin.readline

n = int(input())
w = int(input())

score = 10*n + (20 if n >= 3 else 0) + (50 if n == 5 else 0) - (15 if w > 1000 else 0)
print(max(0, score))