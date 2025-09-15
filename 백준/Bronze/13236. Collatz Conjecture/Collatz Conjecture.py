import sys
input = sys.stdin.readline

n = int(input())
result = [str(n)]
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
         n = 3 * n + 1
    result.append(str(n))
print(' '.join(result))        