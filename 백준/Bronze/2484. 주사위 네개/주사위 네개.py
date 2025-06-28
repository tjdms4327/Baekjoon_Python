import sys
input = sys.stdin.readline
from collections import Counter

def find_exactly_two_duplicates(lst):
    counter = Counter(lst)
    duplicates = [item for item, count in counter.items() if count == 2]
    return duplicates

def receive(nums):
    counter = Counter(nums)

    # All four numbers are the same
    if len(counter) == 1:
        return nums[0] * 5000 + 50000

    # One number appears 3 times
    for num in counter:
        if counter[num] == 3:
            return num * 1000 + 10000

    # Two pairs of numbers
    if len(counter) == 2 and any(count == 2 for count in counter.values()):
        return 2000 + 500 * sum(num for num in counter if counter[num] == 2)

    # Three different numbers
    if len(counter) == 3:
        dup = find_exactly_two_duplicates(nums)
        if dup:
            return 1000 + 100 * dup[0]

    # Default case (last number * 100)
    return nums[-1] * 100

n = int(input())
result = 0
for _ in range(n):
    nums = list(map(int, input().split()))
    nums.sort()
    price = receive(nums)
    if price > result:
        result = price

print(result)
