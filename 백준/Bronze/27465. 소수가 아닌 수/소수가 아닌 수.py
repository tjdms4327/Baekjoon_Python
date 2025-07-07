def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # n의 제곱근까지만 검사
        if n % i == 0:
            return False
    return True

def not_prime(n):
    while is_prime(n):
        n+=1
    return n
        
n=int(input())
print(not_prime(n))