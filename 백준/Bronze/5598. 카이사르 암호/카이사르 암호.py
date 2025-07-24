s=input()
for i in s:
    cur=(ord(i)-3 - ord('A'))%26 + ord('A')
    print(chr(cur), end='')