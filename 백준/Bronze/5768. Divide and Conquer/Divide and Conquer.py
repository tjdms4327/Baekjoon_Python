import sys, math
input = sys.stdin.readline

def divisor_count(num):
    divisor = set()
    for i in range(1, math.isqrt(num)+1):
        if num%i==0:
            divisor.add(i)
            if num%(num//i)==0:
                divisor.add(num//i)
    return len(divisor)

while True:
    m, n = map(int, input().split())
    if m==n==0:
        break
    
    count = []   # num, divisor_count
    for num in range(m, n+1):
        count.append((num, divisor_count(num)))    
    count.sort(key=lambda x:(-x[1], -x[0]))
    
    print(*count[0])