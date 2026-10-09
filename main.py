import tkinter as tk

from PASSWORD_CONSTANTS import *

# ---------------------------- WINDOW ------------------------------- #
window = tk.Tk()
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, padx=20, pady=20)


# ---------------------------- CANVAS ------------------------------- #
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=WHITE)
canvas.grid(column=1, row=0)


# ---------------------------- IMAGE ------------------------------- #
img = tk.PhotoImage(file=LOGO_PNG)
canvas.create_image(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, image=img, anchor=CENTER)


# ---------------------------- LABELS ------------------------------- #
website = tk.Label(text='Website:', font=DEFAULT_FONT, bg=WHITE)
website.grid(column=0, row=1)

username = tk.Label(text='Email/Username:', font=DEFAULT_FONT, bg=WHITE)
username.grid(column=0, row=2)

password = tk.Label(text='Password:', font=DEFAULT_FONT, bg=WHITE)
password.grid(column=0, row=3)


# ---------------------------- LOOP ------------------------------- #
window.mainloop()
