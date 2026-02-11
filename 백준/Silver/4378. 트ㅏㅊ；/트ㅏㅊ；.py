import sys

keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
mapping = {keyboard[i]: keyboard[i-1] for i in range(1, len(keyboard))}

for line in sys.stdin:
    for ch in line:
        if ch == ' ' or ch == '\n':
            sys.stdout.write(ch)
        else:
            sys.stdout.write(mapping[ch])
