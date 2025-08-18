import sys
input = sys.stdin.readline

n = int(input())
if n == 0:
    print('divide by zero')
    exit(0)
else:
    record = list(map(int, input().split()))

avg = sum(record) / n
expect = sum((1 / n) * x for x in record)
print(f'{avg / expect:.2f}')