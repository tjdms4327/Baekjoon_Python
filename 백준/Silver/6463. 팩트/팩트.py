import sys
input = sys.stdin.readline

for line in sys.stdin:
    n = int(line.strip())
    
    result = 1
    i = 2
    while i <= n:
        result *= i
        while result % 10 == 0:
            result //= 10
        result %= 1000000  
        i += 1
        
    print(f'{n:>5} -> {result % 10}')