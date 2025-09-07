import sys
input = sys.stdin.readline

n = int(input())
mascot = input().strip()
k = int(input())

if (mascot == 'annyong' and k%2 == 1) or (mascot == 'induck' and k%2 == 0):
    print(k)
else: 
    if k<n: print(k+1)
    else: print(k-1)