import sys
input = sys.stdin.readline

a1, b1, a2, b2 = map(int, input().split())
gunner =(a1 + b1 + a2 + b2) 
a1, b1, a2, b2 = map(int, input().split())
emma = (a1 + b1 + a2 + b2) 

if gunner < emma:
    print('Emma')
elif gunner == emma:
    print('Tie')
else:
    print('Gunnar')