import sys
input = sys.stdin.readline

T = [int(input()) for _ in range(2)]
while T[-2] >= T[-1]:
    T.append(T[-2] - T[-1])
print(len(T))