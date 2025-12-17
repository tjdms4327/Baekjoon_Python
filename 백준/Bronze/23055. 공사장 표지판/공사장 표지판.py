import sys
input = sys.stdin.readline

n = int(input())

if n <= 4:
    for _ in range(n):
        print('*'*n)
else:
    print('*'*n)
    
    line = []
    for i in range((n-2)//2):
        x = '*' + ' '*i + '*' + ' '*((n-4) - 2*i) + '*' + ' '*i + '*'
        print(x)
        line.append(x)
        
    if n%2 == 1:
        temp = (n-3)//2
        print('*' + ' '*temp + '*' + ' '*temp + '*')
    
    for x in line[::-1]:
        print(x)   
        
    print('*'*n)