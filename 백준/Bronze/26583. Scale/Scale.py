import sys
input = sys.stdin.readline

while True:
    s = list(map(int, input().split()))
    if s == []: break

    result = []
    for i in range(len(s)):
        if i == 0: 
            result.append(s[i] * s[i+1])
        elif i == len(s)-1:
            result.append(s[i-1] * s[i])
        else: 
            result.append(s[i-1] * s[i] * s[i+1])
    print(*result, sep=' ')