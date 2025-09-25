# bronzeII_4072
import sys
input = sys.stdin.readline

while True:
    s = input().strip()
    if s == '#': break
    
    result = []
    for i in s.split():
        result.append(i[::-1])
    print(' '.join(result))