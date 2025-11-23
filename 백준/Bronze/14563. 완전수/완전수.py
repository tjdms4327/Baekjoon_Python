import sys, math
input = sys.stdin.readline

def sum_divisors(n):
    if n == 1:
        return 0
    total = 1
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            total += i
            if i != n//i:
                total += n//i
    return total

def judge_num(n):
    x = sum_divisors(n)
    if x == n:
        return 'Perfect'
    elif x < n:
        return 'Deficient'
    else:
        return 'Abundant'
    

t = int(input())
nums = list(map(int, input().split()))

for n in nums:
    print(judge_num(n))