import sys
input = sys.stdin.readline

p1, p2, p3 = map(int, input().split())
c1, c2, c3 = map(int, input().split())

prices = [p1, p2, p3]
total = sum(prices)
one = total * c1 / 100

two = 0
for i in range(3):
    for j in range(3):
        if i == j: 
            continue
        saving = prices[i] * c2 / 100 + prices[j] * c3 / 100
        two = max(two, saving)


if one > two:
    print(f"one {one:.2f}")
else:
    print(f"two {two:.2f}")