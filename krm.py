import time
import random
import json
from pathlib import Path

with open(Path(__file__).parent / 'words.json', 'r') as wfile:
    words_data = json.load(wfile)

wordtst = random.choice(words_data)
charsleft = wordtst
lettersFound = 0
lives = 10
guessed = set()

def CheckFor_ing(word):
    return word.endswith('ing')
if CheckFor_ing(wordtst):print("HINT: It's a verb")



def lsp(num):
    for i in range (0, num):
        print('', '\n')

def WordLetterCount(word):
    wordfound = ''
    for i in range(0, len(word)):
        wordfound += '-'
    return wordfound

WordFound = WordLetterCount(wordtst)
print('Game starts. You have', lives, 'lives')
lsp(2)

def CheckLetter(char):
    timesfound = 0
    for i in range(0, len(wordtst)):
        if wordtst[i] == char:
            timesfound += 1
    if not timesfound: return False
    if timesfound: return timesfound

#WordFound = WordFound[:1] + '0' + WordFound[1 + 1 :]
while WordFound != wordtst and lives > 0:
    print(WordFound)
    print('You have found', lettersFound, 'letters.')
    usrLetter = input('Enter a letter: ')
    if not usrLetter.isalpha() or len(usrLetter) != 1:
        print('enter letters!')
        continue
    guessed.add(usrLetter)
    timefound = wordtst.count(usrLetter)
    if not timefound:
        lives -=1
        print(f"There's no {usrLetter}. You have {lives} lives left.")
        continue
    print(f"The letter {usrLetter} appears {timefound} times.")
    lettersFound += timefound
    WordFound = ''.join(c if c in guessed else '-' for c in wordtst)

if WordFound == wordtst:
    print('YOU WON!!!')
else:
    print('You Lost! Try Again!')