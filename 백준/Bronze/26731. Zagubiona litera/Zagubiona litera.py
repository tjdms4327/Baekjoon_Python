def missing(letters):
    full=set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    input=set(letters)
    miss=full-input
    return miss.pop()

letters=input().strip()
print(missing(letters))