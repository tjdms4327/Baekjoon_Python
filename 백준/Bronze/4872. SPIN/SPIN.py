# bronzeII_4872
import sys
input = sys.stdin.readline

d = [int(x) for x in input().strip()]

for line in sys.stdin:
    turn = [int(x) for x in line.strip()]
    if not turn: 
        continue
    for i in range(len(d)):
        d[i] += turn[i] % 10

for i in d:
    print(i%10, end='')