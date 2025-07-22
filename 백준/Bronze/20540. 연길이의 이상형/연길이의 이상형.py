mbti = input().strip()

opposite = {
    'E': 'I', 'I': 'E',
    'S': 'N', 'N': 'S',
    'T': 'F', 'F': 'T',
    'J': 'P', 'P': 'J'
}
ideal=''.join(opposite[i] for i in mbti)
print(ideal)
