import sys
input = sys.stdin.readline

def score(a, b):
    if a == b:
        return 1
    if (a == 'R' and b == 'S') or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
        return 2
    return 0

r = int(input())
sang = input().strip()
n = int(input())
friends = [input().strip() for _ in range(n)]
    
    
real_score = 0
for i in range(r):
    for f in friends:
        real_score += score(sang[i], f[i])
print(real_score)


max_score = 0
for i in range(r):
    best = 0
    for hand in "RSP":
        cur = 0
        for f in friends:
            cur += score(hand, f[i])
        best = max(best, cur)
    max_score += best
print(max_score)