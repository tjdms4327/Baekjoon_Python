# bronzeI_3985
import sys
input = sys.stdin.readline

l = int(input())
slice = [0] * (l+1)
n = int(input())

max_expect, expect_index = -1, -1
max_real, real_index = -1, -1
for num in range(1, 1+n):
    pi, ki = map(int, input().split())
    if max_expect < ki-pi+1:
        expect_index = num
        max_expect = ki - pi + 1
    
    for i in range(pi, ki+1):
        if slice[i] == 0:
            slice[i] = num
    if max_real < slice.count(num):
        real_index = num
        max_real = slice.count(num)

print(expect_index)
print(real_index)