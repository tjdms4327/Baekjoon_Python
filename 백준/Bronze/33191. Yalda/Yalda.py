import sys
input=sys.stdin.readline

budget=int(input().strip())
preference=["Watermelon", "Pomegranates", "Nuts"]
nothing=-1
for i in range(3):
    price=int(input().strip())
    if price<=budget: 
        nothing=i
        print(preference[i])
        break
if nothing==-1: print("Nothing")