import sys
input = sys.stdin.readline

pascal = [0]*31
pascal[0] = [1]
pascal[1] = [1, 1]
for i in range(2, 31):
    temp = [0]*(i+1)
    temp[0] = temp[-1] = 1
    for j in range(1, len(pascal[i-1])):
        temp[j] = pascal[i-1][j-1] + pascal[i-1][j]
    pascal[i] = temp
    
n, k = map(int, input().split())
print(pascal[n-1][k-1])
