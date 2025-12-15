import sys
input = sys.stdin.readline

t = int(input())
for i in range(1, 1+t):
    n = int(input())
    print(n)
    
    temp = n
    while len(str(temp)) >= 3:
        temp = temp//10 - temp%10
        print(temp)
        
    if temp == 11:
        print(f'The number {n} is divisible by 11.')
    else:
        print(f'The number {n} is not divisible by 11.')
    if i < n:
        print()