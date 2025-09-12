import sys
input = sys.stdin.readline

t = int(input())
count_bag = 0
for _ in range(t):
    l, w, d, weight = map(float, input().split())
    if (weight <= 7) and ((l + w + d <= 125) or (l <= 56 and w <= 45 and d <= 25)):
        print(1)
        count_bag += 1
    else:
        print(0)
print(count_bag)