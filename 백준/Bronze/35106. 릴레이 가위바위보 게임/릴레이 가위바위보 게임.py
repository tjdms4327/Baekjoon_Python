import sys
input = sys.stdin.readline

n = int(input())
hands = list(map(int, input().split()))

counts = [0]
for i in range(1, 4):
    counts.append(hands.count(i))
    
for i in range(1, 4):
    if counts[i] == n - 1:
        print(i)
        break
for i in range(1, 4):
    if counts[i] == n + 1:
        print(i)
        break
