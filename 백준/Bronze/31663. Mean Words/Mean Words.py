import sys
input = sys.stdin.readline

n = int(input())
s = [input().strip() for _ in range(n)]
length = max(len(word) for word in s) 

for j in range(length):
    col_chars = [ord(s[i][j]) for i in range(n) if j < len(s[i])]
    avg = sum(col_chars) // len(col_chars)
    print(chr(avg), end='')