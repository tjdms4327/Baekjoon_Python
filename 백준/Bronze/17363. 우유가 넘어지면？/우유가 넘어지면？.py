import sys
input = sys.stdin.readline

mapping = {
    '.':'.', 'O':'O', '-':'|', '|':'-',
    '/':'\\', '\\':'/', '^':'<',
    '<':'v', 'v':'>', '>':'^'
}

n, m = map(int, input().split())
picture = [list(input().strip()) for _ in range(n)]

result = []
for col in zip(*picture):
    temp = [mapping[x] for x in col]
    result.append(''.join(temp))

print(*result[::-1], sep='\n')