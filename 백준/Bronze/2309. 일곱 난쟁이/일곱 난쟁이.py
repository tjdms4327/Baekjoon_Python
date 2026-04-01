import sys
input=sys.stdin.readline

heights=[int(input()) for _ in range(9)]
heights.sort()
wrong=sum(heights)-100
#print(wrong)

n,m=0,0
for i in range(9):
    for j in range(i+1, 9):
        if heights[i]+heights[j]==wrong:
            n,m=i,j
for i in range(9):
    if i==n or i==m:
        pass
    else:
        print(heights[i])