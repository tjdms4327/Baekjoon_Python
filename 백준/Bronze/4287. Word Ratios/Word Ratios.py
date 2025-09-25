# bronzeII_4287
import sys
input = sys.stdin.readline

while True:
    s = list(input().strip().split())
    if s == ['#']: break
    
    one, two, three = s
    key = [(ord(two[i]) - ord(one[i]) - ord('a')) % 26 + ord('a') for i in range(len(one))]
    
    result = []
    for i in range(len(three)):
        ascii = (ord(three[i]) + key[i%len(key)] - ord('a')) % 26 + ord('a')
        result.append(chr(ascii))
    print(*s, ''.join(result))