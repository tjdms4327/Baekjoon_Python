import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    A, C = map(int, input().split())
    r, g, b = map(int, input().split())
    
    score_red = A * ((r+1)**2 + g**2 + b**2) + C * min(r+1, g, b)
    score_green = A * (r**2 + (g+1)**2 + b**2) + C * min(r, g+1, b)
    score_blue = A * (r**2 + g**2 + (b+1)**2) + C * min(r, g, b+1)
    
    max_score = max(score_red, score_green, score_blue)
    if max_score == score_red:
        print("RED")
    elif max_score == score_green:
        print("GREEN")
    else:
        print("BLUE")