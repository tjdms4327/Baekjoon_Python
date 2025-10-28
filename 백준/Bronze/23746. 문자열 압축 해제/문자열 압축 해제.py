# bronzeI_23746
import sys
input = sys.stdin.readline

n = int(input())
unzip = {}
for _ in range(n):
    pattern, key = input().strip().split()
    unzip[key] = pattern
    
s = input().strip()
unzip_s = ''.join([unzip[key] for key in s])

s, e = map(int, input().split())
print(unzip_s[s-1:e])