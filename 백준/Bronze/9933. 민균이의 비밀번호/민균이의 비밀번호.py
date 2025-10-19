# bronzeI_9933
import sys
input = sys.stdin.readline

n = int(input())
S = [input().strip() for _ in range(n)]

for s in S:
    if s[::-1] in S:
        len_s = len(s)
        print(len_s, s[len_s//2])
        exit()