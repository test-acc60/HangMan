import random
import json
import time
import subprocess
from pathlib import Path
import tkinter as tk
from tkinter import PhotoImage


with open(Path(__file__).parent / 'words.json', 'r') as wfile:
    words_data = json.load(wfile)

wordtst = random.choice(words_data)
root = tk.Tk()
usrvar = tk.StringVar()
img = PhotoImage(file="temp2.png")
img = img.subsample(2,2)


charsleft = wordtst
lettersFound = 0
lives = 7
guessed = set()
userletter = ''

lettersUsed = ''
WordFound = '-'*len(wordtst)

def loop(count=0):
    color = "#00ff00" if count % 2 == 0 else "blue"
    root.config(bg=color)
    root.after(300, loop, count + 1)


def AddUsedLetters(char):
    global lettersUsed
    lettersUsed += char + ' '
    lrs.config(text=lettersUsed)

lives_images = {
    0: PhotoImage(file="dead.png").subsample(2, 2),
    1: PhotoImage(file="lives1.png").subsample(2, 2),
    2: PhotoImage(file="lives2.png").subsample(2, 2),
    3: PhotoImage(file="lives3.png").subsample(2, 2),
    4: PhotoImage(file="lives4.png").subsample(2, 2),
    5: PhotoImage(file="lives5.png").subsample(2, 2),
    6: PhotoImage(file="lives6.png").subsample(2, 2),
    7: PhotoImage(file="temp2.png").subsample(2, 2)
}
def UpdateLivesImage(livesleft):
    imag = lives_images.get(livesleft, PhotoImage(file="error.png").subsample(2,2))
    imagelabel.config(image=imag)

def UpdateLivesCount(num):
    UpdateLivesImage(num)
    txtt = f'Lives: {num}'
    livecount.config(text=txtt)

def UpdateLabel(strr):
    wrdfou.config(text=strr)

def UpdateWarns(strr):
    txt.config(text=strr)



def Submit():
    global WordFound, lives, lettersFound
    if lettersFound >= len(wordtst):
        lettersFound = len(wordtst)-1
    userletter = usrvar.get()
    usrvar.set('')

    if not userletter.isalpha() or len(userletter) != 1:
        UpdateWarns('Enter only letters!')
        return
    guessed.add(userletter)
    timesfound = wordtst.count(userletter)

    if not timesfound:
        lives -=1
        UpdateLivesCount(lives)
        AddUsedLetters(userletter)
        message = f"There is no letter {userletter}"
    else:
        UpdateLivesCount(lives)
        lettersFound += timesfound
        WordFound = ''.join(c if c in guessed else '-' for c in wordtst)
        message = f'The letter {userletter} appears {timesfound} times. You have found {lettersFound} letters so far'
    UpdateLabel(WordFound)

    if WordFound == wordtst:
        message = ('Correct! You won!')
        imag = PhotoImage(file="yay.png").subsample(2,2)
        imagelabel.config(image=imag)
        imagelabel.image = imag
        loop()
        subm.config(state=tk.DISABLED)
    elif lives <= 0:
        message = (f'You lost! The word was {wordtst}')
        subm.config(state=tk.DISABLED)
    UpdateWarns(message)





root.title('Hangman')
label = tk.Label(root, text='Hangman Game. You have 7 lives', font=('Arial', 20)).pack()
Entry = tk.Entry(root, textvariable=usrvar, font=('Arial', 10, 'normal')).pack(padx=0, pady=20)
txt = tk.Label(root, text='Enter any letter to begin', font=('Arial', 12), fg='red')
txt.pack(padx=0, pady=21)
subm = tk.Button(root, text='Submit', font=('Arial', 24), bg='green', command=Submit, state=tk.NORMAL)
subm.pack(padx=0, pady=21)
wrdfou = tk.Label(root, text=WordFound, font=('Arial', 35))
wrdfou.place(relx=0.5, rely=0.44, anchor='center')
root.minsize(600, 600)
root.maxsize(600, 600)
livecount = tk.Label(root, text='Lives: 7', font=('Arial', 20, 'bold'))
livecount.place(relx=0.1, rely=0.42, anchor='w')
imagelabel = tk.Label(root)
imagelabel.place(relx=0.5, rely=0.75, anchor='center')
imagelabel.config(image=lives_images[7])
txxt = tk.Label(root, text='Letters used:', font=('Arial', 15), fg='blue')
txxt.place(relx=0.94, rely=0.4, anchor='e')
lrs = tk.Label(root, text='', font=('Arial', 17))
lrs.place(relx=0.7, rely=0.43)

root.mainloop()
