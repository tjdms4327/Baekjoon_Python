import sys
input=sys.stdin.readline

cards={'S':[], 'B':[], 'K':[], 'V':[]}
for _ in range(51):
    pattern, n=input().strip().split()
    cards[pattern].append(int(n))

full = set(range(1, 14))
for p, nums in cards.items():
    if len(nums)!=13:
        print(p, (full-set(nums)).pop())