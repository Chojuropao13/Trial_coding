import time
import pyautogui
import tkinter as tk

def screenshoot () :
    name = int(round(time.time() * 1000))
    name = "C:/Users/drago/Downloads/Project python/hasil ss/{}.png".format(name)
    
    img = pyautogui.screenshot(name)
    img.show()
    
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button (
    frame,
    text = "Take Screenshoot",
    command = screenshoot )

button.pack(side=tk.LEFT)
close = tk.Button (
    frame,
    text="QUIT",
    command=quit)
close.pack(side=tk.LEFT)

root.mainloop()