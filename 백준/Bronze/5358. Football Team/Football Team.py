table=str.maketrans('iIeE', 'eEiI')

try:
    while True:
        name=input()
        name=name.translate(table)
        print(name)
except:
    exit(0)