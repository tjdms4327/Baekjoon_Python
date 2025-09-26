# bronzeII_6765
import sys
input = sys.stdin.readline

k = int(input())

line1 = ['*'*k + 'x'*k + '*'*k] * k 
line2 = [' '*k + 'x'*k + 'x'*k] * k
line3 = ['*'*k + ' '*k + '*'*k] * k
print(*line1, sep='\n')
print(*line2, sep='\n')
print(*line3, sep='\n')