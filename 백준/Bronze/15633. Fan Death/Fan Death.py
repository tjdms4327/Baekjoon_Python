# bronzeIII_15633
import sys
input = sys.stdin.readline

def divisor(n):
    divisor_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisor_list.append(i)
            if n//i not in divisor_list and n%(n//i) == 0:
                divisor_list.append(n//i)
    return divisor_list
    
n = int(input())
print(sum(divisor(n)) * 5 - 24)