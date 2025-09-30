# tkinter-intro.py - Beautiful Edition 

from tkinter import *
from tkinter import font

# --- Event Handler Functions ---

def button_clicked():
    """
    Handles the main button click event.
    It gets text from the entry box, provides visual feedback,
    and updates the main label.
    """
    new_text = input_entry.get().strip()

    if new_text and new_text != "Type something...":
        my_label.config(text=new_text, fg="#08dd33")
        window.after(500, lambda: my_label.config(fg="#54ac55"))
        input_entry.delete(0, END)
        on_entry_focus_out(None)
    else:
        my_label.config(text="Please enter some text!", fg="#dc2626")
        window.after(1000, lambda: my_label.config(text="Enter your text below", fg="#334155"))

def on_entry_focus_in(event):
    """Clears the placeholder text when the entry widget gains focus."""
    if input_entry.get() == "Type something...":
        input_entry.delete(0, END)
        input_entry.config(fg="#0f172a")

def on_entry_focus_out(event):
    """Restores the placeholder text if the entry widget is empty when it loses focus."""
    if not input_entry.get():
        input_entry.insert(0, "Type something...")
        input_entry.config(fg="#64748b")

# --- Hover Effect Functions (for new light button style) ---

def on_button_hover(event):
    """Changes primary button background to a slightly darker gray on hover."""
    button.config(bg="#e2e8f0")

def on_button_leave(event):
    """Restores primary button background when mouse leaves."""
    button.config(bg="#f1f5f9")

def on_new_button_hover(event):
    """Changes secondary button background to a slightly darker gray on hover."""
    new_button.config(bg="#e2e8f0")

def on_new_button_leave(event):
    """Restores secondary button background when mouse leaves."""
    new_button.config(bg="#f1f5f9")

# --- Window Setup ---
window = Tk()
window.title("✨ My Beautiful GUI")
window.geometry("600x500")
window.config(bg="#f8fafc")
window.resizable(True, True)

# --- Font Creation ---
title_font = font.Font(family="Helvetica", size=32, weight="bold")
subtitle_font = font.Font(family="Helvetica", size=14)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# --- UI Structure using Frames ---
header_frame = Frame(window, bg="#f8fafc")
header_frame.pack(pady=30, padx=40, fill=X)

title_label = Label(header_frame, text="🎨 Beautiful GUI", font=title_font, bg="#f8fafc", fg="#0f172a")
title_label.pack()

subtitle_label = Label(header_frame, text="A modern approach to tkinter", font=subtitle_font, bg="#f8fafc", fg="#475569")
subtitle_label.pack(pady=(5, 0))

# --- Main Content Frame with Shadow Effect ---
shadow_frame = Frame(window, bg="#e2e8f0")
shadow_frame.place(relx=0.5, rely=0.55, anchor=CENTER, relwidth=0.85, relheight=0.55)

content_frame = Frame(window, bg="white", relief=FLAT, bd=0)
content_frame.place(relx=0.5, rely=0.54, anchor=CENTER, relwidth=0.85, relheight=0.55)

# --- Widgets inside the Content Frame ---
my_label = Label(content_frame, text="Enter your text below", font=("Helvetica", 18), bg="white", fg="#334155")
my_label.pack(pady=(40, 20), expand=True)

input_entry = Entry(
    content_frame,
    width=25,
    font=("Helvetica", 14),
    fg="#64748b",
    bg="#f1f5f9",
    relief=FLAT,
    bd=0
)
input_entry.insert(0, "Type something...")
input_entry.pack(ipady=8, ipadx=10, pady=20)

input_entry.bind("<FocusIn>", on_entry_focus_in)
input_entry.bind("<FocusOut>", on_entry_focus_out)
input_entry.bind("<Return>", lambda e: button_clicked())

buttons_frame = Frame(content_frame, bg="white")
buttons_frame.pack(pady=30, expand=True)

# --- Updated Buttons with Light Background and Colored Text ---
# Primary Button with a light background and indigo text.
button = Button(
    buttons_frame,
    text="✓ Update Text",
    command=button_clicked,
    font=button_font,
    bg="#f1f5f9",         # Light gray background
    fg="#38c0ca",         # Indigo text color
    activebackground="#e2e8f0", # Darker gray for active/press
    activeforeground="#38c0ca", # Text color remains the same when pressed
    relief=FLAT,
    bd=0,
    padx=30,
    pady=12,
    cursor="hand2"
)
button.pack(side=LEFT, padx=10)
button.bind("<Enter>", on_button_hover)
button.bind("<Leave>", on_button_leave)

# Secondary Button with a light background and blue text.
new_button = Button(
    buttons_frame,
    text="ℹ Info",
    command=lambda: my_label.config(text="This is a beautiful tkinter app!", fg="#0369a1"),
    font=button_font,
    bg="#f1f5f9",         # Light gray background
    fg="#38c0ca",         # Blue text color
    activebackground="#e2e8f0", # Darker gray for active/press
    activeforeground="#38c0ca", # Text color remains the same when pressed
    relief=FLAT,
    bd=0,
    padx=30,
    pady=12,
    cursor="hand2"
)
new_button.pack(side=LEFT, padx=10)
new_button.bind("<Enter>", on_new_button_hover)
new_button.bind("<Leave>", on_new_button_leave)

# --- Footer ---
footer_label = Label(window, text="Made with ❤️ using Python & Tkinter", font=("Helvetica", 9), bg="#f8fafc", fg="#64748b")
footer_label.pack(side=BOTTOM, pady=15)

# --- Start the GUI Main Loop ---
window.mainloop()
