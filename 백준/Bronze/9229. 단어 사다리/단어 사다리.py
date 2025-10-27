# bronzeI_9229
import sys
input = sys.stdin.readline

while True:
    words = []
    while True:
        s = input().strip()
        if s == '#':
            break
        words.append(s)
    if not words:  
        break

    correct = True
    for i in range(1, len(words)):
        if len(words[i]) != len(words[i-1]):
            correct = False
            break
        diff = sum(1 for a, b in zip(words[i-1], words[i]) if a != b)
        if diff != 1:
            correct = False
            break

    print('Correct' if correct else 'Incorrect')
