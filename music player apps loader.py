Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
import pygame
pygame 2.5.2 (SDL 2.28.3, Python 3.11.4)
Hello from the pygame community. https://www.pygame.org/contribute.html
pygame.mixer.init()
#Inisialisasi Pygame mixernya
os.chdir(r"C:\Users\drago\Downloads") #Target direktori yang di inginkan
nama_file_lagu = "The Greatest Show _ Stradivari Orchestra.mp3"
try :
    #operator lagu
    pygame.mixer.music.load(nama_file_lagu)
    pygame.mixer.music.play(()
... except FileNotFoundEror :
...     
SyntaxError: '(' was never closed
>>> try :
...     #operator lagu
...     pygame.mixer.music.load(nama_file_lagu)
...     pygame.mixer.music.play()
... except FileNotFoundEror:
...     print(f"anda kurang beruntung hari ini, coba lagi dengan pasangan anda")
... 
...     
