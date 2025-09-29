# bronzeIII_29684
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0: break
    
    A = list(map(int, input().split()))
    diff = [abs(i - 2023) for i in A]
    print(1 + diff.index(min(diff)))