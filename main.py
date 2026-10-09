import tkinter as tk

from PASSWORD_CONSTANTS import *

# ---------------------------- WINDOW ------------------------------- #
window = tk.Tk()
window.config(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, padx=20, pady=20, bg=WHITE)
window.resizable(width=False, height=False)


# ---------------------------- CANVAS ------------------------------- #
canvas = tk.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=WHITE, highlightthickness=0)
canvas.grid(column=1, row=0)


# ---------------------------- IMAGE ------------------------------- #
img = tk.PhotoImage(file=LOGO_PNG)
canvas.create_image(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, image=img, anchor=CENTER)


# ---------------------------- LABELS ------------------------------- #
website = tk.Label(text='Website:', font=DEFAULT_FONT, bg=WHITE)
website.grid(column=0, row=1, sticky=WE)

username = tk.Label(text='Email/Username:', font=DEFAULT_FONT, bg=WHITE)
username.grid(column=0, row=2, sticky=WE)

password = tk.Label(text='Password:', font=DEFAULT_FONT, bg=WHITE)
password.grid(column=0, row=3, sticky=WE)


# ---------------------------- ENTRIES ------------------------------- #
website_entry = tk.Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky=WE)

username_entry = tk.Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky=WE)

password_entry = tk.Entry()
password_entry.grid(column=1, row=3, sticky=WE)


# ---------------------------- BUTTONS ------------------------------- #
generate_button = tk.Button(text='Generate Password')
generate_button.grid(column=2, row=3, sticky=WE)

add_button = tk.Button(text='Add')
add_button.grid(column=1, row=4, columnspan=2, sticky=WE)


# ---------------------------- LOOP ------------------------------- #
window.mainloop()
