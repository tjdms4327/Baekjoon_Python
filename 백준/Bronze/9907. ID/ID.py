import sys
input = sys.stdin.readline

num = list(input().strip())
weight = [2, 7, 6, 5, 4, 3, 2]
sum = 0
for i in range(7):
    sum += (int(num[i]) * weight[i])
    
mapping = {0:'J', 1:'A', 2:'B', 3:'C',
           4:'D', 5:'E', 6:'F', 7:'G',
           8:'H', 9:'I', 10:'Z'}
print(mapping[sum%11])