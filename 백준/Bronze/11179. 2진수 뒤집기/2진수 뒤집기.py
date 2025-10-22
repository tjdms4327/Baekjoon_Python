# bronzeI_11179
import sys
input = sys.stdin.readline

n = int(input())

n2 = bin(n)[2:]
reverse_bin = n2[::-1]
print(int(reverse_bin, 2))