# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
letterCount = {}
ignoreChar = {
    ' ',
    ',',
    '.',
    "'",
    "\n",
    '"',
    ';',
    ':',
    '-',
    '?',
    '!',
    'â',
    '€',
    '”',
    '(',
    '1',
    ')'
}

with open("ciphertext.txt") as file:
    read = file.read()

for i in read:
    if i not in ignoreChar:
        if i in letterCount:
            letterCount[i] += 1
        elif i != '':
            letterCount[i] = 1

letterList = list(letterCount.items())
letterList.sort(key = lambda l: l[1], reverse = True)

decode = {}
decodedWords = ""
decodeKey = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U','G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

for i,touple in enumerate(letterList):
    decode[touple[0]] = decodeKey[i]

for i in read:
    if i in decode:
        decodedWords += decode[i]
    else:
        decodedWords += i

print(decodedWords)