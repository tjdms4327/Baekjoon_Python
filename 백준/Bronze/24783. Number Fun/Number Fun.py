# bronzeIII_24783
import sys
input = sys.stdin.readline

def possible_operation(nums):
    c = nums[-1]
    a, b = sorted(nums[:2], reverse=True)
    if a+b == c:
        return 'Possible'
    elif a-b == c:
        return 'Possible'
    elif a*b == c:
        return 'Possible'
    elif a/b == c:
        return 'Possible'
    return 'Impossible'
    
t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))
    print(possible_operation(nums))