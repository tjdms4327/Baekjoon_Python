# bronzeII_5222
import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    key_s, s = input().strip().split()
    key = [ord(x) - ord('A') for x in key_s]
    
    result = []
    for i in range(len(s)):
        shifted = (ord(s[i]) + key[i%len(key_s)] - ord('A')) % 26 + ord('A')
        result.append(chr(shifted))
    print(f"Ciphertext: {''.join(result)}")