# bronzeIII_34447.py
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    key, num = input().strip().split()
    key = int(key)
    nums = list(map(int, num))
    
    result = []
    for i in nums:
        print((i + key) % 10, end='')
    print()