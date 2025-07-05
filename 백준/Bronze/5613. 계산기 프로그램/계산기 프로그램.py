import sys
input = sys.stdin.readline

def cal(result, n, k):
    if n == '+':
        return result + k
    elif n == '-':
        return result - k
    elif n == '*':
        return result * k
    elif n == '/' and k != 0:
        return result // k

result = int(input().strip()) 
while True:
    n = input().strip() 
    if n == '=':
        break
    k = int(input().strip())
    result = cal(result, n, k)
print(result)
