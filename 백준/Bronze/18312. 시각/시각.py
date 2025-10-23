# bronzeII_18312
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
for h in range(0, n+1):
    for m in range(0, 60):
        for s in range(0, 60):
            time = str(h).zfill(2) + str(m).zfill(2) + str(s).zfill(2)
            if str(k) in time:
                count += 1
print(count)