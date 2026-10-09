import tkinter as tk

from PASSWORD_CONSTANTS import *

# window
window = tk.Tk()
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# canvas
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='blue')
canvas.pack(padx=20, pady=20, anchor='center', fill='both', expand=1)

# image logo
img = tk.PhotoImage(file='./logo.png')
canvas.create_image(200//2, 200//2, image=img, anchor='center')

# loop
window.mainloop()