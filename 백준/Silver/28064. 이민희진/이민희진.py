# silverV_28064
import sys
input = sys.stdin.readline

n = int(input())
names = [input().strip() for _ in range(n)]

count = 0
for i in range(n):
    for j in range(i+1, n):
        s, t = names[i], names[j]
        connected = False
        
        for k in range(1, min(len(s), len(t))+1):
            if s[:k] == t[-k:] or s[-k:] == t[:k]:
                connected = True
                break
        if connected:
            count += 1

print(count)