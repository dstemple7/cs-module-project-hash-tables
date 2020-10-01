import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
wordsArray = words.split()
wordsStart = []
wordsNext = {}

for i,word in enumerate(wordsArray):
    if not word.islower():
        wordsStart.append(word)
    if word in wordsNext:
        wordsNext[word].append(wordsArray[i + 1])
    else:
        if i + 1 < len(wordsArray):
            wordsNext[word] = [wordsArray[i + 1]]

# TODO: construct 5 random sentences
# Your code here
punct = {".", "?", "!"}

def randSentence():
    output = word = random.choice(wordsStart)
    while len(word) < 1 or (not word[-1] in punct and not word[-2] in punct):
        word = random.choice(wordsNext[word])
        output = output + " " + word
    return output

print(randSentence())
print(randSentence())
print(randSentence())
print(randSentence())
print(randSentence())

