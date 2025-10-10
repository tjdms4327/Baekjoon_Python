# bronzeIII_20360
import sys
input = sys.stdin.readline

n = int(input())

bin_n = str(bin(n))[2:][::-1]
for i in range(len(bin_n)):
    if bin_n[i] == '1':
        print(i, end=' ')