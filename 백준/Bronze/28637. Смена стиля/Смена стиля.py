import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    for i, ch in enumerate(input().strip()):
        if ch.isupper():
            print(ch.lower() if i == 0 else '_' + ch.lower(), end='')
        else:
            print(ch, end='')
    print()