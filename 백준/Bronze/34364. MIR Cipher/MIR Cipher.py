# bronzeIII_34364.py
import sys
input = sys.stdin.readline

n, s = input().strip().split()
for i in range(int(n)):
    ASCII = (ord(s[i]) + (2**i) - ord('A')) % 26 + ord('A')
    print(chr(ASCII), end='')