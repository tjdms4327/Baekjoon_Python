# bronzeIII_24606
import sys
input = sys.stdin.readline

password1 = input().strip()
password2 = input().strip()

possible = 1
for i in range(4):
    if password1[i] != password2[i]:
        possible *= 2
print(possible)