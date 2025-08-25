import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
adjective = [input().strip() for _ in range(n)]
noun = [input().strip() for _ in range(m)]

for a in adjective:
    for n in noun:
        print(f'{a} as {n}')