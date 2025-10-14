# bronzeII_1362
import sys
input = sys.stdin.readline

case = 0
while True:
    case += 1
    o, w = map(int, input().split())
    if o == w == 0: break
    
    alive = True
    while True:
        ef, n = input().split()
        if ef == '#' and n == '0':
            if not alive:
                print(f"{case} RIP")
            elif o * 0.5 < w < 2 * o:
                print(f"{case} :-)")
            else:
                print(f"{case} :-(")
            break

        n = int(n)
        if alive:
            if ef == 'E':
                w -= n
            else:
                w += n
            if w <= 0:
                alive = False