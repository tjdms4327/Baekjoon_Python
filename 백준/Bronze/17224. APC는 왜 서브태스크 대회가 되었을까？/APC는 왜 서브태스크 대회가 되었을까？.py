# bronzeI_17224
import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())

easy, hard = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    
    if b <= l:
        hard += 1
    elif a <= l:
        easy += 1

if k <= hard:
    score = 140 * k
else:
    score = 140 * hard + 100 * min(k-hard, easy) 
print(score)