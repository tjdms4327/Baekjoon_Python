import sys
input = sys.stdin.readline

s = input().strip()

if s.endswith('eh?'):
    print('Canadian!')
else:
    print('Imposter!')