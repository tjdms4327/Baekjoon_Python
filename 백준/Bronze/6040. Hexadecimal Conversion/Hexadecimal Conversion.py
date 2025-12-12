import sys
input = sys.stdin.readline

hexa = int(input().strip(), 16)
print(oct(hexa)[2:])