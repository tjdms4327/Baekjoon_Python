import sys
input = sys.stdin.readline

x1, x2 = map(int, input().split())
a, b, c, d, e = map(int, input().split())

def calculus(x):
    return a*(x**3)//3 + (b-d)*(x**2)//2 + (c-e)*x

print(calculus(x2) - calculus(x1))