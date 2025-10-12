# bronzeIII_27130
import sys
input = sys.stdin.readline

num1 = int(input())
num2 = input().strip()
print(num1)
print(num2)

for digit in reversed(num2): 
    print(num1 * int(digit))

print(num1 * int(num2))