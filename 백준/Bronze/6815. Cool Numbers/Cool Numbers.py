import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

count = 0
k = 1
while True:
    x = k**6
    if a <= x <= b:
        count += 1
    elif x > b:
        break
    k += 1
print(count)