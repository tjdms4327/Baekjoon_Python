# bronzeIII_25840
import sys
input = sys.stdin.readline

n = int(input())
birth = [input().strip() for _ in range(n)]
print(len(set(birth)))