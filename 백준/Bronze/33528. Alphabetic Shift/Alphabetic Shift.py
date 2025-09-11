import sys
input = sys.stdin.readline

s = input().strip()
for i in range(26):
    shifted = ""
    for c in s:
        shifted += chr((ord(c) - ord('A') - i) % 26 + ord('A'))
    print(shifted)