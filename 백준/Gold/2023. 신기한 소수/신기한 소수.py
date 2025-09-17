import sys
sys.setrecursionlimit(10000) # 최대 재귀 깊이
input = sys.stdin.readline

n = int(input()) # 자릿수

def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == n:
        print(number)
    else:
        for i in range(1, 10, 2): # 짝수면 탐색할 필요없음
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)
            

# 일의 자리 소수는 2, 3, 5, 7뿐임
DFS(2)
DFS(3)
DFS(5)
DFS(7)