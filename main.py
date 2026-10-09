import tkinter as tk

from PASSWORD_CONSTANTS import *

# ---------------------------- WINDOW ------------------------------- #
window = tk.Tk()
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

# ---------------------------- CANVAS ------------------------------- #
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='white')
canvas.pack(padx=20, pady=20, anchor='center', fill='both', expand=1)

# ---------------------------- IMAGE ------------------------------- #
img = tk.PhotoImage(file='./logo.png')
canvas.create_image(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, image=img, anchor='center')

# ---------------------------- LOOP ------------------------------- #
window.mainloop()