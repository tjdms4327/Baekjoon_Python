# bronzeIII_34366
import sys
input = sys.stdin.readline

m = int(input())
score = []
sum_m = []
for _ in range(m):
    s = list(map(int, input().split()))
    
    score.extend(s[1:])
    sum_m.append(sum(s[1:]))

print(max(score))
print(min(score))
print(max(sum_m))
print(min(sum_m))