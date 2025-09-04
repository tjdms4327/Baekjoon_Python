import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
scores = [0] * n

card_idx = {val: i for i, val in enumerate(cards)}
sorted_cards = sorted(cards)
for i, a in enumerate(sorted_cards):
    for j in range(2*a, sorted_cards[-1]+1, a):
        if j in card_idx:
            scores[card_idx[a]] += 1
            scores[card_idx[j]] -= 1
print(*scores)
