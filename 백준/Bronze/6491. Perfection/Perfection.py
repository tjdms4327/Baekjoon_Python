import sys

nums=list(map(int, sys.stdin.read().split()))
nums=nums[:-1]



from math import sqrt
def divisors(num):
    divisor=set()
    for i in range(1, int(sqrt(num))+1):
        if num%i==0:
            divisor.add(i)
            divisor.add(num//i)
    return list(divisor)
    
for i in nums:
    divisor=divisors(i)
    sum_without_self=sum(divisor)-i

    #print(i, sum_without_self)
    if i==sum_without_self: # 완전수
        print(i, 'PERFECT')
    elif i>sum_without_self: # 부족수
        print(i, 'DEFICIENT')
    else: # 과잉수
        print(i, 'ABUNDANT')
    