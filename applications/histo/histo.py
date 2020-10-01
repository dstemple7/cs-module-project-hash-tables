# ignore the following: ' : ; , . - + = / \ | [ ] { } ( ) * ^ &
ignoreChar = {
    '"': '',
    ':': '',
    ';': '',
    ',': '',
    '.': '',
    '-': '',
    '+': '',
    '=': '',
    '/': '',
    '\\': '',
    '|': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    '(': '',
    ')': '',
    '*': '',
    '^': '',
    '&': ''}
# Your code here

fileFiltered = ""
histo = {}

with open("robin.txt") as file:
    robin = file.read()
    robin = robin.lower()

for i in robin:
    if i in ignoreChar:
        fileFiltered += ignoreChar[i]
    else:
        fileFiltered += i

words = fileFiltered.split()

for word in words:
    if word in histo:
        histo[word] += 1
    else:
        histo[word] = 1

listHistoItems = list(histo.items())
listHistoItems = sorted(listHistoItems)
listHistoItems.sort(key = lambda x: x[1], reverse = True)

for touple in listHistoItems:
    print(f"{touple[0]}{(17 - len(touple[0])) * ' '}{touple[1] * '#'}")