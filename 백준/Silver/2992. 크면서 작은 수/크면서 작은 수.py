import sys
input=sys.stdin.readline

from itertools import permutations

x=input().strip()
num_x=int(x)
length=len(x)



result=[]
for comb in permutations(x, length):
    number=int(''.join(comb))
    if number>num_x:
        result.append(number)
        
if result:
    print(min(result))
else:
    print(0)