# bronzeI_14696
import sys
input = sys.stdin.readline

def winner(A, B):
    shape_A = [A[1:].count('4'), A[1:].count('3'),A[1:].count('2'), A[1:].count('1')]
    shape_B = [B[1:].count('4'), B[1:].count('3'), B[1:].count('2'), B[1:].count('1')]
    
    for i in range(4):
        if shape_A[i] > shape_B[i]:
            return 'A'
        elif shape_B[i] > shape_A[i]:
            return 'B'
        else:
            continue
    return 'D'

n = int(input())
for _ in range(n):
    A = list(input().strip().split())
    B = list(input().strip().split())
    
    print(winner(A, B))