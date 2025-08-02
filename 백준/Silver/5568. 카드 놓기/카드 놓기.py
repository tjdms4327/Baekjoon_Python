import sys
input=sys.stdin.readline

from itertools import permutations

n=int(input().strip())
k=int(input().strip())
cards=[input().strip() for _ in range(n)]


result_set=set()
for comb in permutations(cards, k):
    number=''.join(comb)
    result_set.add(number)
print(len(result_set))