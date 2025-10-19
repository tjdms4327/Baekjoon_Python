# bronzeI_6996
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    A, B = input().strip().split()
    
    if sorted(A) == sorted(B):
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')