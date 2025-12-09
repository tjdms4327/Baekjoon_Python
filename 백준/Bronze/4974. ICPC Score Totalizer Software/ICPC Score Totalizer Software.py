import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    scores = [int(input()) for _ in range(n)]
    scores.sort()
    
    print(sum(scores[1:-1]) // (n-2))