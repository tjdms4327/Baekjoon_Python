import sys

lines = []
for line in sys.stdin.read().splitlines():
    lines.append(line.strip().split())

max_cols = max(len(line) for line in lines)

max_len = [0] * max_cols
for line in lines:
    for i, word in enumerate(line):
        max_len[i] = max(max_len[i], len(word))

for line in lines:
    result = ''
    for i, word in enumerate(line):
        result += word
        if i != len(line) - 1:         # 마지막 단어면 공백 X
            result += ' ' * (max_len[i] - len(word) + 1)
    print(result)
