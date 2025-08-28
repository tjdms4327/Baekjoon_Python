import sys
input = sys.stdin.readline

n = int(input())
s = input().strip().split()

prohibit = ['he', 'him', 'she', 'her']
cnt = sum(s.count(i) for i in prohibit)
print(cnt)