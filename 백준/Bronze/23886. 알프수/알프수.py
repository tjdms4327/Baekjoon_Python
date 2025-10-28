# bronzeI_23886
import sys
input = sys.stdin.readline

nums = list(map(int, input().strip()))

alpsoo = True
slope = None
for i in range(len(nums)-1):
    if slope == None:
        slope = nums[i+1] - nums[i]
        if slope <= 0:
            alpsoo = False
            break
        continue
    
    cur_slope = nums[i+1] - nums[i]
    if cur_slope == 0:
        alpsoo = False
        break
    elif cur_slope * slope > 0:
        if slope != cur_slope:
            alpsoo = False
            break
    else:
        slope = cur_slope
if slope >= 0:
    alpsoo = False

if alpsoo:
    print('ALPSOO')
else:
    print('NON ALPSOO')