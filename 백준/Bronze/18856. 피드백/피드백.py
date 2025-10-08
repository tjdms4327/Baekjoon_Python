# bronzeIII_18856
import sys
input = sys.stdin.readline

def prime(x):
    for i in range(x, 1001):
        prime = True
        for j in range(2, int(i**0.5)+1):
            if i%j==0:
                prime = False
                break
        if prime:
            return i

n = int(input())
print(n)
print(*range(1, n), prime(n))