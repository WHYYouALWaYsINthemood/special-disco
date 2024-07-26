from tkinter import *
root = Tk()
root.title("Colors")
root.geometry("600x400")

label_mutable = Label(root)
label_immutable = Label(root)
label_tkinter = Label(root)

dictionary = {'Red': 'Red has a range of symbolic meanings through many different cultures, including life, health, vigor, war, courage, anger, love and religious fervor. The common thread is that all these require passion',
              'Blue': 'The color blue represents both the sky and the sea and is associated with open spaces, freedom, intuition, imagination, inspiration, and sensitivity. Blue also represents meanings of depth, trust, loyalty, sincerity, wisdom, confidence, stability, faith, and intelligence',
              'Green': 'In spiritual terms, the color green implies beginnings, new growth, vibrant health, and other ideas connected with life, rebirth, and renewal. If youre noticing green in your environment or dreams, you might be discovering new aspects of yourself, beginning a new phase of life, or undergoing a renewal'}

def Mutable():
    label_mutable["text"] = dictionary['Red']

def Immutable():
    label_immutable["text"] = dictionary['Blue']

def Tkinter():
    label_tkinter["text"] = dictionary['Green']

button_mutable = Button(root, text = "Meaning of Red", command = Mutable)
button_mutable.place(relx = 0.5, rely = 0.2,anchor = CENTER)
label_mutable.place(relx = 0.5, rely = 0.3,anchor = CENTER)

button_immutable = Button(root, text = "Meaning of Blue", command = Immutable)
button_immutable.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label_immutable.place(relx = 0.5, rely = 0.5, anchor = CENTER)

button_tkinter = Button(root, text = "Meaning of Green", command = Tkinter)
button_tkinter.place(relx = 0.5, rely = 0.6, anchor = CENTER)
label_tkinter.place(relx = 0.5, rely = 0.7, anchor = CENTER)

root.mainloop()