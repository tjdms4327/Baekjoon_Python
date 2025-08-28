import sys
input = sys.stdin.readline

n = int(input())
coffee = input().strip()

awake = 0
carry = 0
for i in coffee:
    if i == '1':
        awake += 1
        carry = max(2, carry)
    else:
        if carry:
            awake += 1
            carry -=1
print(awake)