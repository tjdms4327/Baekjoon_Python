# bronzeIII_11800
import sys
input = sys.stdin.readline

def same_num(nums):
    x = nums[0]
    if x == 1:
        return 'Habb Yakk'
    elif x == 2:
        return 'Dobara'
    elif x == 3:
        return 'Dousa'
    elif x == 4:
        return 'Dorgy'
    elif x == 5:
        return 'Dabash'
    else:
        return 'Dosh'

def different_num(nums):
    a, b = nums
    if a == 6 and b == 5:
        return 'Sheesh Beesh'
    
    mapping = {1:'Yakk', 2:'Doh', 3:'Seh',
               4:'Ghar', 5:'Bang', 6:'Sheesh'}
    return mapping[a]+' '+mapping[b]

t = int(input())
for case in range(t):
    nums = list(map(int, input().split()))
    
    print(f'Case {case+1}: ', end='')
    if len(set(nums)) == 1:
        print(same_num(nums))
    else:
        nums.sort(reverse=True)
        print(different_num(nums))