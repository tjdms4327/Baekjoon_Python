import sys
input=sys.stdin.readline
import math

n,a,b=map(int, input().split())

FizzBuzz, Fizz, Buzz=0,0,0
lcm=(a*b)//math.gcd(a,b) #최소공배수

for i in range(1, n+1):
    if i%(lcm)==0: FizzBuzz+=1
    elif i%a==0: Fizz+=1
    elif i%b==0: Buzz+=1
print(Fizz, Buzz, FizzBuzz)