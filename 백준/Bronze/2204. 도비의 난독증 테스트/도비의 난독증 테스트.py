# bronzeI_2204
import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    
    words = [input().strip() for _ in range(n)]
    min_word = min(words, key=lambda x:x.lower())
    print(min_word)