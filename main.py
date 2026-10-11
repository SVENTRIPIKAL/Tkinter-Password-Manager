import json
import random
import tkinter as tk
import tkinter.messagebox as info_box
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import pyperclip

from PASSWORD_CONSTANTS import *


# ---------------------------- FUNCTIONS ------------------------------- #
def generate_password():
    """ adds a random 42 length password to password field & user clipboard """
    _lowercase = list(ascii_lowercase)
    _uppercase = list(ascii_uppercase)
    _digits = list(digits)
    _punctuation = list(punctuation)

    all_symbols = _lowercase + _uppercase + _digits + _punctuation

    new_password = EMPTY.join([random.choice(all_symbols) for _ in range(FORTY_TWO)])

    # save to password field
    password_entry.focus()
    password_entry.delete(first=ZERO, last=tk.END)
    password_entry.insert(index=ZERO, string=new_password)

    # save to clipboard
    pyperclip.copy(new_password)
    info_box.showinfo(message=CLIPBOARD_MESSAGE)


def clear_fields():
    """ clears entry fields & refocuses cursor to first entry """
    website_entry.delete(ZERO, tk.END)
    username_entry.delete(ZERO, tk.END)
    password_entry.delete(ZERO, tk.END)
    website_entry.focus()


def entry_fields_complete(*args) -> bool:
    """ returns True if all fields contain text """
    return not EMPTY in args


def save_json(save_data:  dict[str, dict[str, str]]):
    """ reads & updates JSON data to file path """
    with open(FILE_PATH, R_PLUS) as file:
        file_data = json.load(fp=file)
        file_data.update(save_data)
        file.seek(ZERO)
        json.dump(obj=file_data, fp=file, indent=4)
        file.truncate()


def create_file():
    """ create file with empty JSON data """
    with open(FILE_PATH, W.lower()) as file:
        json.dump(obj={}, fp=file)


def save_information():
    """ saves information from entry fields to file 'IGNORE' """
    we_text, ue_text, pe_text = website_entry.get(), username_entry.get(), password_entry.get()
    # verify fields
    if entry_fields_complete(we_text, ue_text, pe_text):
        # save data as dictionary
        save_data = {
            we_text.upper() : {
                USERNAME : ue_text,
                PASSWORD : pe_text
            }
        }
        # dump as JSON string
        json_data = json.dumps(obj=save_data, indent=4)
        # display validate response
        user_response = info_box.askyesno(
            title=None, message=VALIDATE_MESSAGE, icon=info_box.QUESTION,
            detail=json_data, default=info_box.NO
        )
        if user_response:
            while True:
                try:
                    # save to file
                    save_json(save_data)
                except (ValueError, FileNotFoundError):
                    create_file()
                else:
                    # display success
                    info_box.showinfo(message=SUCCESS_MESSAGE)
                    clear_fields()
                    break
    else: # display error
        info_box.showerror(message=ERROR_MESSAGE)


def search(json_key: str):
    """ displays JSON key file data or Error message """
    with open(FILE_PATH, R) as file:
        file_data = json.load(fp=file)
        json_data = file_data.get(json_key)
        if json_data:
            _username, _password = json_data.values()
            info_box.showinfo(message=f'USERNAME: {_username}\n\nPASSWORD: {_password}')
        else:
            info_box.showerror(message=CREDENTIALS_MESSAGE)


def find_password():
    """ checks file for credential information if available """
    we_text = website_entry.get().upper()
    while True:
        try:
            search(json_key=we_text)
        except (ValueError, FileNotFoundError):
            create_file()
        else:
            break


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
website = tk.Label(text=f'{WEBSITE.title()}:', font=DEFAULT_FONT, bg=WHITE)
website.grid(column=0, row=1, sticky=WE, padx=5)

username = tk.Label(text=f'{USERNAME.title()}:', font=DEFAULT_FONT, bg=WHITE)
username.grid(column=0, row=2, sticky=WE, padx=5)

password = tk.Label(text=f'{PASSWORD.title()}:', font=DEFAULT_FONT, bg=WHITE)
password.grid(column=0, row=3, sticky=WE, padx=5)


# ---------------------------- ENTRIES ------------------------------- #
website_entry = tk.Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky=WE, padx=5, pady=5)

username_entry = tk.Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky=WE, padx=5, pady=5)

password_entry = tk.Entry()
password_entry.grid(column=1, row=3, columnspan=2, sticky=WE, padx=5, pady=5)


# ---------------------------- BUTTONS ------------------------------- #
add_button = tk.Button(text='Search', command=find_password)
add_button.grid(column=3, row=1, sticky=WE, padx=5, pady=5)

generate_button = tk.Button(text='Generate Password', command=generate_password)
generate_button.grid(column=3, row=3, sticky=E, padx=5, pady=5)

add_button = tk.Button(text='Add', command=save_information)
add_button.grid(column=1, row=4, columnspan=2, sticky=WE, padx=5, pady=5)


# ---------------------------- LOOP ------------------------------- #
window.mainloop()
