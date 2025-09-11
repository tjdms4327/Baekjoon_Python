import sys
input = sys.stdin.readline

s = input().strip()
if s[-1] in 'aeiouns':
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] in 'aeiou':
            count += 1
            if count == 2:
                print(i+1)
                sys.exit()
    else: # 모음이 두 개 미만
        print(-1)
else:
    for i in range(len(s)-1, -1, -1):
        if s[i] in 'aeiou':
            print(i+1)
            break
    else:
        print(-1)