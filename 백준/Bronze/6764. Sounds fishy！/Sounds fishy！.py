fishes=[]
for _ in range(4):
    fish=int(input())
    fishes.append(fish)

if max(fishes)==min(fishes):
    print("Fish At Constant Depth")
elif fishes[0]<fishes[1] and fishes[1]<fishes[2] and fishes[2]<fishes[3]:
    print("Fish Rising")
elif fishes[0]>fishes[1] and fishes[1]>fishes[2] and fishes[2]>fishes[3]:
    print("Fish Diving")
else:
    print("No Fish")