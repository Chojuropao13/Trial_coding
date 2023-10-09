Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
>>> from time import strftime
>>> def time() :
...     string = strftime( '%H: %M: %S %p')
...     label.config(text=string)
...     label.after(1000, time)
... 
>>> root = tk.Tk()
>>> root.title('Jam Digital')
''
>>> label = tk.Label(root, font=('Times', 40, 'bold'), bg='pink', foreground='white')
>>> label.pack(anchor='center')
>>> time()
>>> root.mainloop()
