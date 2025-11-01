# bronzeII_9437
import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if line == '0':
        break

    n, p = map(int, line.split())

    for i in range(1, n // 4 + 1):
        pages = [4 * i - 3, 4 * i - 2, n - (4 * i - 3) + 1, n - (4 * i - 2) + 1]
        if p in pages:
            pages.remove(p)
            print(*sorted(pages))
            break
