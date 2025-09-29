# bronzeIII_34301
import sys
input = sys.stdin.readline

n = int(input())
bill = [0] * 5

bill[4] = n // 150 ; n %= 150
bill[3] = n // 30 ; n %= 30
bill[2] = n // 15 ; n %= 15
bill[1] = n // 5 ; n %= 5
bill[0] = n 
print(*bill)