# bronzeII_12813
import sys
input = sys.stdin.readline

a = int(input(), 2)
b = int(input(), 2)

length = 100000
mask = 2**length - 1 # 길이 100000의 모두 1로 이루어진 이진수

print(bin(a&b)[2:].zfill(length))
print(bin(a|b)[2:].zfill(length))
print(bin(a^b)[2:].zfill(length))
print(bin(a^mask)[2:].zfill(length)) 
print(bin(b^mask)[2:].zfill(length))