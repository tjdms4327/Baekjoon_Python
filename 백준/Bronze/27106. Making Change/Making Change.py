import sys
input = sys.stdin.readline

p = int(input())

p = 100 - p

cnt = []
for x in [25, 10, 5, 1]:
    temp = p//x
    
    cnt.append(temp)
    p -= temp*x
    
print(*cnt)