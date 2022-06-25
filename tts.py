from tkinter import *
from gtts import gTTS
from playsound import playsound


root = Tk()
root.geometry("350x300")
root.configure(bg="ghost white")
root.title("Text To Speech")


Label(root, text="Text to Speech Label", font="arial 20 bold", bg="white smoke").pack()
Label(text="McConnell", font="arial 15 bold", bg="white smoke", width="20").pack(side="bottom")


text_input = StringVar()
Label(root, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20, y=60)

entry_field = Entry(root, textvariable=text_input, width='50')
entry_field.place(x=20, y=100)


def text_to_speech():
    text = entry_field.get()
    speech = gTTS(text)
    speech.save('speech.mp3')
    playsound('speech.mp3')


def Exit():
    root.destroy()

def Reset():
    text_input.set('')


Button(root, text="Play", font='arial 15 bold', command=text_to_speech, width='4').place(x=25, y=140)

Button(root, font='arial 15 bold', text='Exit', width='4', command=Exit, bg="OrangeRed1").place(x=100, y=140)

Button(root, font="arial 15 bold", text="Reset", width='6', command=Reset).place(x=175, y=140)

root.mainloop()