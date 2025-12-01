import sys
input = sys.stdin.readline

name = input().strip()
if name.startswith('F'):
    print('Foundation')
elif name.startswith('C'):
    print('Claves')
elif name.startswith('V'):
    print('Veritas')
else:
    print('Exploration')