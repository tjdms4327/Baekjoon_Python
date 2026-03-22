import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
               
    prizes = []
    for _ in range(n):
        line = list(map(int, input().split()))
        _, *needed, value = line
        prizes.append((value, needed))
    prizes.sort(reverse=True)
    
    stickers = [0] + list(map(int, input().split()))

    total = 0
    for value, needed in prizes:
        while all(stickers[s] > 0 for s in needed):
            total += value
            for s in needed:
                stickers[s] -= 1

    print(total)