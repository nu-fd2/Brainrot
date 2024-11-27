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

    def close_on_enter(event):
        if event.keysym == 'Return':
            root.destroy()
    
    root.bind('<Return>', close_on_enter)

    label = tk.Label(root, text="Press Enter to close")
    label.pack()
    
    # Schedule window destruction
    # root.after(4000, lambda: root.quit())
    
    root.mainloop()




    

def cat():
    show_image_and_play_audio("cat.png", "cataudio.mp3")

def yipeee():
    show_image_and_play_audio("yipee.png", "yippeeeee.mp3")

if input(f"what is your skin color?[black/white] ")!= "white":
    cat()
else:
    yipeee()

if input(f"do you hate jews?[yes/no] ") != "yes":
    cat()
else:
    yipeee()

if input(f"was 9/11 an inside job?[yes/no] ") != "yes":
    cat()
else:
    yipeee()

if input(f"do u support LGTVQ+?[yes/no] ") != "no":
    cat()
else:
    yipeee()
