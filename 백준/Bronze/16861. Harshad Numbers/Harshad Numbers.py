# bronzeIII_16861
import sys
input = sys.stdin.readline

n = int(input().strip())
while True:
    if n % sum(list(map(int, str(n)))) == 0:
        print(n)
        break
    n += 1