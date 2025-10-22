# silverV_25757
import sys
input = sys.stdin.readline

member_num = {'Y':1, 'F':2, 'O':3}

n, game = input().strip().split()
names = set(input().strip() for _ in range(int(n)))

print(len(names) // member_num[game])