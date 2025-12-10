import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    
    for i in range(k):
        if 1 <= i <= k//2-1:
            print('#'+'.'*(i-1)+'#'+'.'*(k-2*i-2)+'#'+'.'*(i-1)+'#')            
        elif i == k//2:
            print('#'+'.'*((k-3)//2)+'#'+'.'*((k-3)//2)+'#')          
        else:
            print('#'+'.'*(k-2)+'#')            