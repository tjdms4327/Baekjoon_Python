import sys
input = sys.stdin.readline

l = int(input())

arcane_lv = [200, 210, 220, 225, 230, 235]
arcane_reduce1 = [210, 220, 225, 230, 235, 245]
arcane_reduce2 = [220, 225, 230, 235, 245, 250]
arcane = []
for i in range(6):
    if l < arcane_lv[i]:
        arcane.append(0)
    elif l < arcane_reduce1[i]:
        arcane.append(500)
    elif l < arcane_reduce2[i]:
        arcane.append(300)
    else:
        arcane.append(100)

grandis_lv = [260, 265, 270, 275, 280, 285, 290]
grandis_reduce1 = [265, 270, 275, 280, 285, 290, 295]
grandis_reduce2 = [270, 275, 280, 285, 290, 295, 300]
grandis = []
for i in range(7):
    if l < grandis_lv[i]:
        grandis.append(0)
    elif l < grandis_reduce1[i]:
        grandis.append(500)
    elif l < grandis_reduce2[i]:
        grandis.append(300)
    else:
        grandis.append(100)

print(*arcane)
print(*grandis)