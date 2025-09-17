import sys
input = sys.stdin.readline

n = int(input())
n -= 2013 # 2013년 F9

first = ord('A') + (n + 5) % 12
second = (n + 9) % 10
print(chr(first)+str(second))