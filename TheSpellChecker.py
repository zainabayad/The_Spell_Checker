from textblob import TextBlob
from tkinter import *

def checkspell():
    b = TextBlob(e.get())
    corrected_text = Label(root, text = str(b.correct()))
    corrected_text.pack()

root = Tk()
root.title('SpellCheck')
root.geometry('600x300')

head = Label(root, text='SpellCheck',font=('times', 14 , 'bold'))
head.pack()
e = Entry(root, width=200,borderwidth=10)
e.pack()
b = Button(root, text = 'Check', font=('times', 8 , 'bold'), fg = 'white', bg = 'brown', command = check)
b.pack()
root.mainloop()