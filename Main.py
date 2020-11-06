from tkinter import *
from tkinter import messagebox
from pygame import mixer
import sys
root = Tk()
root.configure(bg='blue')
root.title('Piano')
mixer.init()
root.attributes('-fullscreen',True)
def Yes_no():
    c = messagebox.askokcancel('Piano','ARE you sure you want to exit ?')
    print(c)
    if c == 'False':
        pass
    else:
        sys.exit(0)
def play_music(val):
    if val == 1:
        mixer.music.load(f'C.mp3')
        mixer.music.play()
    elif val == 2:
        mixer.music.load(f'D.mp3')
        mixer.music.play()
    elif val == 3:
        mixer.music.load(f'E.mp3')
        mixer.music.play()
    elif val == 4:
        mixer.music.load(f'F.mp3')
        mixer.music.play()
    elif val == 5:
        mixer.music.load(f'G.mp3')
        mixer.music.play()
    elif val == 6:
        mixer.music.load(f'A.mp3')
        mixer.music.play()
    elif val == 7:
        mixer.music.load(f'B.mp3')
        mixer.music.play()
    elif val == 8:
        mixer.music.load(f'C1.mp3')
        mixer.music.play()
C_btn = Button(root,pady=200,padx=50,text='C\n◼',font=('Helvatica',25),command = lambda : play_music(1)).grid(row=1,column=1)
D_btn = Button(root,pady=200,padx=50,text='D\n◼',font=('Helvatica',25),command = lambda : play_music(2)).grid(row=1,column=2)
E_btn = Button(root,pady=200,padx=50,text='E\n◼',font=('Helvatica',25),command = lambda : play_music(3)).grid(row=1,column=3)
F_btn = Button(root,pady=200,padx=50,text='F\n◼',font=('Helvatica',25),command = lambda : play_music(4)).grid(row=1,column=4)
G_btn = Button(root,pady=200,padx=50,text='G\n◼',font=('Helvatica',25),command = lambda : play_music(5)).grid(row=1,column=5)
A_btn = Button(root,pady=200,padx=50,text='A\n◼',font=('Helvatica',25),command = lambda : play_music(6)).grid(row=1,column=6)
B_btn = Button(root,pady=200,padx=50,text='B\n◼',font=('Helvatica',25),command = lambda : play_music(7)).grid(row=1,column=7)
C1_btn = Button(root,pady=200,padx=50,text='C\n◾',font=('Helvatica',25),command = lambda : play_music(8)).grid(row=1,column=8)
Exit_btn = Button(root,pady=75,padx=540,text='Exit ?',font=('Helvatica',25),command = Yes_no).grid(row=2,column=1,columnspan=8)
root.mainloop()