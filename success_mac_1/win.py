import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import PhotoImage

import subprocess

root = tk.Tk()
root.geometry("343x345")

image = PhotoImage(file="cat.png")

label = tk.Label(root, image=image)
label.pack()

audio_file = 'cataudio.mp3'

subprocess.run(['afplay', audio_file])

root.mainloop()
