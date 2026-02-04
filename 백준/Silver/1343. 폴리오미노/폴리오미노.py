import sys
input = sys.stdin.readline

boards = list(input().strip().split('.'))

result = []
for x in boards:
    length = len(x)
    if length % 2 != 0:
        print(-1)
        sys.exit()
    elif length % 4 == 0:
        result.append('AAAA'*(length//4))
    else:
        result.append('AAAA'*(length//4)+'BB')

print('.'.join(result))