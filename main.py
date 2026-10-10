import random
import tkinter as tk
import tkinter.messagebox as info_box
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

from PASSWORD_CONSTANTS import *


# ---------------------------- FUNCTIONS ------------------------------- #
def generate_password():
    """ adds a random 42 length password to password entry field """
    _lowercase = list(ascii_lowercase)
    _uppercase = list(ascii_uppercase)
    _digits = list(digits)
    _punctuation = list(punctuation)

    all_symbols = _lowercase + _uppercase + _digits + _punctuation

    new_password = [random.choice(all_symbols) for _ in range(FORTY_TWO)]

    password_entry.delete(first=ZERO, last=tk.END)
    password_entry.insert(index=ZERO, string=EMPTY.join(new_password))


def clear_fields():
    """ clears entry fields & refocuses cursor to first entry """
    website_entry.delete(ZERO, tk.END)
    username_entry.delete(ZERO, tk.END)
    password_entry.delete(ZERO, tk.END)
    website_entry.focus()


def entry_fields_complete(*args) -> bool:
    """ returns True if all fields contain text """
    return not EMPTY in args


def save_information():
    """ saves information from entry fields to file 'IGNORE' """
    we_text, ue_text, pe_text = website_entry.get(), username_entry.get(), password_entry.get()
    # verify fields
    if entry_fields_complete(we_text, ue_text, pe_text):
        save_data = f'WEBSITE: {we_text} | EMAIL/USERNAME: {ue_text} | PASSWORD: {pe_text}'
        # display validate response
        user_response = info_box.askyesno(
            title=None, message=VALIDATE_MESSAGE, icon=info_box.QUESTION,
            detail=save_data.replace(' | ', '\n'), default=info_box.NO
        )
        if user_response:
            # save to file
            with open(FILE_PATH, A) as writer:
                writer.write(f'{save_data}\n')
            # display success
            info_box.showinfo(message=SUCCESS_MESSAGE)
            clear_fields()

    else: # display error
        info_box.showerror(message=ERROR_MESSAGE)


# ---------------------------- WINDOW ------------------------------- #
window = tk.Tk()
window.title(PROGRAM_NAME)
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
website.grid(column=0, row=1, sticky=WE, padx=5)

username = tk.Label(text='Email/Username:', font=DEFAULT_FONT, bg=WHITE)
username.grid(column=0, row=2, sticky=WE, padx=5)

password = tk.Label(text='Password:', font=DEFAULT_FONT, bg=WHITE)
password.grid(column=0, row=3, sticky=WE, padx=5)


# ---------------------------- ENTRIES ------------------------------- #
website_entry = tk.Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky=WE, padx=5, pady=5)

username_entry = tk.Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky=WE, padx=5, pady=5)

password_entry = tk.Entry()
password_entry.grid(column=1, row=3, sticky=WE, padx=5, pady=5)


# ---------------------------- BUTTONS ------------------------------- #
generate_button = tk.Button(text='Generate Password', command=generate_password)
generate_button.grid(column=2, row=3, sticky=WE, padx=5, pady=5)

add_button = tk.Button(text='Add', command=save_information)
add_button.grid(column=1, row=4, columnspan=2, sticky=WE, padx=5, pady=5)


# ---------------------------- LOOP ------------------------------- #
window.mainloop()
