Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> from tkinter import filedialog
>>> from pygame import mixer
pygame 2.5.2 (SDL 2.28.3, Python 3.11.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
>>> class player:
...     def __init__(self, window):
...          window.geometry('320x100')
...          window.title("Cinta tak semanis itu bestie")
...          window.resizable(0, 0)
...          Load = Button(window, text="Load", width=10, font=("Times", 10), command=self.load)
...          Play = Button(window, text="Play", width=10, font=("Times", 10), command=self.play)
...          Pause = Button(window, text="Pause", width=10, font=("Times", 10), command=self.pause)
...          Stop = Button(window, text="Stop", width=10, font=("Times", 10), command=self.stop)
...          Load.place(x=0, y=20)
...          Play.place(x=110, y=20)
...          Pause.place(x=220, y=20)
...          Stop.place(x=110, y=60)
...          self.music_file = None
...          self.playing_state = False
...     def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state = True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()

        
new_root = Tk()
player_app = player(new_root)
new_root.mainloop()
