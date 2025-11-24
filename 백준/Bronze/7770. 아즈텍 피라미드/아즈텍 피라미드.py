import sys
input = sys.stdin.readline

n = int(input())


temp = 0
while n > 0:
    floor = temp**2 + (temp+1)**2
    
    if n < floor:
        break
    n -= floor
    temp += 1
print(temp)