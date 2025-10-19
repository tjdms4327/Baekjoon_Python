# bronzeI_1526
import sys
input = sys.stdin.readline

n = int(input())
for x in range(n, 0, -1):
    if set(str(x)) <= {'4', '7'}:
        print(x)
        exit()