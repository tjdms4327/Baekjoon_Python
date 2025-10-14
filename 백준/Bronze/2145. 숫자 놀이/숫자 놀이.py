# bronzeII_2145
import sys
input = sys.stdin.readline

while True:
    n = list(map(int, input().strip()))
    if n == [0]: break
    
    while len(n) != 1:
        n = list(map(int, str(sum(n))))
    print(*n)