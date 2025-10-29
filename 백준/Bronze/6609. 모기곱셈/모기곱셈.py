# bronzeII_6609
import sys
input = sys.stdin.readline

for line in sys.stdin.read().splitlines():
    m, p, l, e, r, s, n = map(int, line.split())

    for _ in range(n):
        temp = m
        m = p//s
        p = l//r
        l = temp * e
    print(m)    