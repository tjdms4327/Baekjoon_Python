# bronzeI_10448
import sys
input = sys.stdin.readline

T = [i * (i + 1) // 2 for i in range(1, 46)]
    
def sum_3(k):
    for i in T:
        for j in T:
            for m in T:
                if i + j + m == k:
                    return 1
    return 0
    
t = int(input())
for _ in range(t):
    k = int(input()) 
    print(sum_3(k))