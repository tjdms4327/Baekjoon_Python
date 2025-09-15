import sys
input = sys.stdin.readline

def getDivisorCount(n):
    lst_divisor = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            lst_divisor.append(i)
            if (i**2) != n: # 제곱수 방지
                lst_divisor.append(n // i)
    return len(lst_divisor)
    
c = int(input())
for _ in range(c):
    n = int(input())
    print(n, getDivisorCount(n))