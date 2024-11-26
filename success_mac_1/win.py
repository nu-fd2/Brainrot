import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import subprocess
import threading
import tkinter as tk
from tkinter import PhotoImage

def play_audio(audio_file):
    subprocess.run(['afplay', audio_file])

def show_image_and_play_audio(image_file, audio_file):
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)  # Handle window close button

    image = PhotoImage(file=image_file)
    width = image.width()
    height = image.height()
    root.geometry(f"{width}x{height}")

    label = tk.Label(root, image=image)
    label.pack()

    # Keep a reference to the image to prevent garbage collection
    label.image = image

    # Start the audio playback in a separate thread
    audio_thread = threading.Thread(target=play_audio, args=(audio_file,))
    audio_thread.daemon = True  # Make thread daemon so it terminates with main program
    audio_thread.start()

    # Schedule window destruction
    root.after(4000, lambda: root.quit())
    
    root.mainloop()

question = "what is your skin color?[black/white] "
correct_answer = "white"
user_answer = input(f"{question}")
if user_answer != correct_answer:
    show_image_and_play_audio("cat.png", "cataudio.mp3")
else:
    show_image_and_play_audio("yippee-happy.gif", "yippeeeee.mp3")

question = "do you hate jews?[yes/no] "
correct_answer = "yes"
user_answer = input(f"{question}")
if user_answer != correct_answer:
    show_image_and_play_audio("cat.png", "cataudio.mp3")
else:
    show_image_and_play_audio("yippee-happy.gif", "yippeeeee.mp3")

question = "was 9/11 an inside job?[yes/no] "
correct_answer = "yes"
user_answer = input(f"{question}")
if user_answer != correct_answer:
    show_image_and_play_audio("cat.png", "cataudio.mp3")
else:
    show_image_and_play_audio("yippee-happy.gif", "yippeeeee.mp3")

question = "ar u gei?[yes/no] "
correct_answer = "no"
user_answer = input(f"{question}")
if user_answer != correct_answer:
    show_image_and_play_audio("cat.png", "cataudio.mp3")
else:
    show_image_and_play_audio("yippee-happy.gif", "yippeeeee.mp3")