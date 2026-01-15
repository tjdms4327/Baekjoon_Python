import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

cand = []
for name in names:
    print(f'? {name}', flush=True)
    r1 = int(input())
    print(f'? {name}', flush=True)
    r2 = int(input())
    
    if r1 == 1 or r2 == 1:
        print(f'! {name}', flush=True)
        sys.exit()