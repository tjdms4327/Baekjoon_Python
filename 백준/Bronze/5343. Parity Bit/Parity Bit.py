import sys
input = sys.stdin.readline

for case in range(int(input())):
    n = input().strip()

    count = 0
    for i in range(0, len(n), 8):
        chunk = n[i:i+8]
        one = chunk.count('1')
    
        if n[-1] == '0':
            if one % 2 == 1:
                count += 1
        else:
            if one % 2 == 1:
                count += 1
    print(count)