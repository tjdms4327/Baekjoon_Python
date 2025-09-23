# bronzeIII_21339.py
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
d, s = map(int, input().split())

if n == k:
    print('impossible')
else:
    difficulty = (n * d - k * s) / (n - k)
    if not 0 <= difficulty <= 100:
        print('impossible')
    else:
        print(difficulty)