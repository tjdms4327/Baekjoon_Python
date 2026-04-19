import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    real = int(a)*int(b)
    
    if len(a) < len(b):
        a, b = b, a
    
    diff = len(a)-len(b)
    res = a[:diff]
    for i in range(len(b)):
        res += str(int(a[diff+i])*int(b[i]))
    
    if int(res) == real:
        print(1)
    else:
        print(0)