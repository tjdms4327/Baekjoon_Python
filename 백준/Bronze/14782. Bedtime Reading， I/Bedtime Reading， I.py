# bronzeIII_14782
import sys
input = sys.stdin.readline

def sum_prime(n):
    prime = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            prime.append(i)
            if n % (n//i) == 0 and n//i not in prime:
                prime.append(n//i)
    return sum(prime)

i = int(input())
print(sum_prime(i))