# bronzeI_17202
import sys
input = sys.stdin.readline

A = list(map(int, input().strip()))
B = list(map(int, input().strip()))

result = []
for i in range(8):
    result.append(A[i])
    result.append(B[i])
    
while len(result) > 2:
    new = []
    for i in range(len(result) - 1):
        new.append((result[i] + result[i + 1]) % 10)
    result = new

print(f"{result[0]}{result[1]}")
