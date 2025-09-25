# bronzeII_5100
import sys
input = sys.stdin.readline

while True:  
    t = int(input())
    if t == 0: break
    
    clothes = [0, 0, 0, 0, 0]
    for _ in range(t):
        n = input().strip()
        if n.isdigit():
            if int(n) >= 12:
                clothes[1] += 1
            else:
                clothes[2] += 1
        elif n in 'ML': 
            clothes[0] += 1
        elif n == 'S':
            clothes[3] += 1
        else:
            clothes[4] += 1
    print(*clothes, sep=' ')