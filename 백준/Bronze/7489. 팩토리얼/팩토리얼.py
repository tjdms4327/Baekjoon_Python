import sys
input = sys.stdin.readline

factorial = [1]
for i in range(1, 1001):
    factorial.append(factorial[-1] * i)

t = int(input())
for _ in range(t):
    n = int(input())
    
    result = str(factorial[n])
    for ch in result[::-1]:
        if ch != '0':
            print(ch)
            break
    