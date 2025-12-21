import sys, math
input = sys.stdin.readline

lcm = math.lcm(23, 28, 33)

case = 0
while True:
    p, e, i, d = map(int, input().split())
    if p==e==i==d==-1:
        break
    
    case += 1
    x = (p*5544 + e*14421 + i*1288) % lcm
    if x <= d:
        x += lcm
    
    print(f"Case {case}: the next triple peak occurs in {x - d} days.")