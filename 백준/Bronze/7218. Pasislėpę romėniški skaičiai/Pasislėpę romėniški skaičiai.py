n=int(input())
s=input()

mapping={
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
    7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"
}
for num, roman in mapping.items():
    if roman in s:
        print(num, end=' ')