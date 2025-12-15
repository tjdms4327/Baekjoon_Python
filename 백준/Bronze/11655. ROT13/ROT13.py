import sys
input = sys.stdin.readline

s = input()

for ch in s:
    if ch.isupper():
        result = chr((ord(ch) - ord('A') + 13)%26 + ord('A'))
    elif ch.islower():
       result = chr((ord(ch) - ord('a') + 13)%26 + ord('a'))
    else:
        result = ch
    print(result, end='')