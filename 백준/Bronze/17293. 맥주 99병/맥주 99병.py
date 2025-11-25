import sys
input = sys.stdin.readline

def bottle(n):
    if n == 0:
        return "no more bottles"
    elif n == 1:
        return "1 bottle"
    else:
        return f"{n} bottles"

n = int(input())
k = n
while k > 0:
    b = bottle(k)
    print(f"{b} of beer on the wall, {b} of beer.")
    
    if k - 1 >= 0:
        next_bottle = bottle(k - 1)
    print(f"Take one down and pass it around, {next_bottle} of beer on the wall.")
    print()
    
    k -= 1
    
print("No more bottles of beer on the wall, no more bottles of beer.")
print(f"Go to the store and buy some more, {bottle(n)} of beer on the wall.")
