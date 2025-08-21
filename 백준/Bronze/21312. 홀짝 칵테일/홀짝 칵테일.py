import sys
input = sys.stdin.readline

from math import prod

cocktail = list(map(int, input().split()))


odd = False
result =1
for i in range(3):
    if cocktail[i] % 2 == 1:
        result *= cocktail[i]
        odd = True
 
if odd:
    print(result)
else: 
    print(prod(cocktail))
