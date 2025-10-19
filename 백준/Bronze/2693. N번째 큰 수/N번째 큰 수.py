# bronzeI_2693
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    A = list(map(int, input().split()))
    A.sort()
    
    print(A[-3])