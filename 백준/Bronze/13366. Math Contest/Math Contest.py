import sys
print = sys.stdout.write

t = int(input())
data = sys.stdin.read().split()  # 남은 모든 입력을 한 번에 읽음

for x in data:
    digit_sum = sum(int(c) for c in x)
    if digit_sum % 9 == 0:
        print('YES\n')
    else:
        print('NO\n')