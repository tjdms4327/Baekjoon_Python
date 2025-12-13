import sys
input = sys.stdin.readline

factorial = [0, 1]
for i in range(2, 367):
    factorial.append(factorial[-1] * i)

while True:
    n = int(input())
    if n == 0:
        break

    input()  # 빈 줄 처리

    result = str(factorial[n])
    count = [0] * 10
    for i in range(10):
        count[i] = result.count(str(i))

    print(f"{n}! --")
    for i in range(5):
        print(f"   ({i}){count[i]:5d} ", end='')
    print()
    for i in range(5, 10):
        print(f"   ({i}){count[i]:5d} ", end='')
    print()
