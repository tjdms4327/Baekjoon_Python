# bronzeII_5618
import sys, math
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

g = math.gcd(nums[0], nums[1])
if n == 3:
    g = math.gcd(g, nums[2])

divisors = []
for i in range(1, int(g**0.5) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:
            divisors.append(g // i)
for d in sorted(divisors):
    print(d)