import sys
input = sys.stdin.readline

s1, s2 = map(int, input().split())

for _ in range(s1):
    ans, man = input().strip().split()
    if ans != man:
        print('Wrong Answer')
        sys.stdin.read()
        exit(0)

for _ in range(s2):
    ans, man = input().strip().split()
    if ans != man:
        print('Why Wrong!!!')
        sys.stdin.read()
        exit(0)

print('Accepted')