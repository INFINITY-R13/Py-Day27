# Other_Tkinter_Widgets.py - Beautiful Edition

from tkinter import *
from tkinter import font

# --- Main Window Setup ---
window = Tk()
window.title("✨ Tkinter Widget Showcase")
window.geometry("700x650")
window.config(bg="#f8fafc") # Light background for the whole window

# --- Font Creation ---
# Defining fonts centrally for a consistent look.
title_font = font.Font(family="Helvetica", size=24, weight="bold")
subtitle_font = font.Font(family="Helvetica", size=11)
widget_font = font.Font(family="Helvetica", size=11)
button_font = font.Font(family="Helvetica", size=11, weight="bold")

# --- Main Content Frame ---
# A single main frame to hold all content, with padding.
main_frame = Frame(window, bg="#f8fafc", padx=20, pady=20)
main_frame.pack(fill=BOTH, expand=True)

# --- Header ---
header_frame = Frame(main_frame, bg="#f8fafc")
header_frame.pack(fill=X, pady=(0, 20))

title_label = Label(header_frame, text="🎨 Widget Showcase", font=title_font, bg="#f8fafc", fg="#0f172a")
title_label.pack()

subtitle_label = Label(header_frame, text="An example of various styled tkinter widgets", font=subtitle_font, bg="#f8fafc", fg="#475569")
subtitle_label.pack()

# --- Output Display Label ---
# This label will be updated by other widgets instead of printing to the console.
output_frame = Frame(main_frame, bg="#e2e8f0", relief=FLAT, bd=0)
output_frame.pack(fill=X, pady=10, ipady=5)
output_label = Label(output_frame, text="Output will be shown here...", font=widget_font, bg="#e2e8f0", fg="#334155")
output_label.pack(pady=10, padx=15, anchor="w")

# --- Scrollable Frame for Widgets ---
# Canvas and Scrollbar setup to make the content scrollable
canvas = Canvas(main_frame, bg="white", highlightthickness=0)
scrollbar = Scrollbar(main_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas, bg="white", padx=20, pady=20)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# --- Widget Functions ---
# Each function now updates the output_label.
def button_action():
    output_label.config(text="Button clicked!")

def spinbox_used():
    output_label.config(text=f"Spinbox value: {spinbox.get()}")

def scale_used(value):
    output_label.config(text=f"Scale value: {value}")

def checkbutton_used():
    state = "ON" if checked_state.get() == 1 else "OFF"
    output_label.config(text=f"Checkbutton is {state}")

def radio_used():
    output_label.config(text=f"Radiobutton selected: Option {radio_state.get()}")

def listbox_used(event):
    try:
        selection = listbox.get(listbox.curselection())
        output_label.config(text=f"Listbox selection: {selection}")
    except TclError:
        pass # Ignore error if nothing is selected

# --- Widget Definitions and Styling ---

# Using a grid layout within the scrollable_frame for alignment
row_counter = 0

# --- Button ---
Label(scrollable_frame, text="Button:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
button = Button(
    scrollable_frame, text="Click Me", command=button_action, font=button_font, bg="#f1f5f9",
    fg="#4338ca", relief=FLAT, bd=0, padx=20, pady=8, cursor="hand2",
    activebackground="#e2e8f0", activeforeground="#4338ca"
)
button.grid(row=row_counter, column=1, sticky="ew", padx=10)
row_counter += 1

# --- Entry ---
Label(scrollable_frame, text="Entry:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
entry = Entry(scrollable_frame, width=30, font=widget_font, fg="#0f172a", bg="#f1f5f9", relief=FLAT, bd=0)
entry.insert(END, string="Some text to begin with.")
entry.grid(row=row_counter, column=1, sticky="ew", padx=10, ipady=5)
row_counter += 1

# --- Text ---
Label(scrollable_frame, text="Text:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
text = Text(scrollable_frame, height=4, width=30, font=widget_font, fg="#0f172a", bg="#f1f5f9", relief=FLAT, bd=0)
text.insert(END, "Example of multi-line text entry.")
text.grid(row=row_counter, column=1, sticky="ew", padx=10, ipady=5)
row_counter += 1

# --- Spinbox ---
Label(scrollable_frame, text="Spinbox:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
spinbox = Spinbox(
    scrollable_frame, from_=0, to=10, width=5, command=spinbox_used, font=widget_font,
    fg="#0f172a", bg="#f1f5f9", relief=FLAT, bd=0, buttonbackground="#f1f5f9"
)
spinbox.grid(row=row_counter, column=1, sticky="w", padx=10, ipady=4)
row_counter += 1

# --- Scale ---
Label(scrollable_frame, text="Scale:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
scale = Scale(
    scrollable_frame, from_=0, to=100, command=scale_used, orient=HORIZONTAL,
    font=widget_font, bg="white", fg="#0f172a", relief=FLAT, bd=0,
    troughcolor="#e2e8f0", activebackground="#4f46e5", highlightthickness=0
)
scale.grid(row=row_counter, column=1, sticky="ew", padx=10)
row_counter += 1

# --- Checkbutton ---
Label(scrollable_frame, text="Checkbutton:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
checked_state = IntVar()
checkbutton = Checkbutton(
    scrollable_frame, text="Is On?", variable=checked_state, command=checkbutton_used,
    font=widget_font, bg="white", fg="#0f172a", activebackground="white", activeforeground="#0f172a",
    selectcolor="#f1f5f9", relief=FLAT, bd=0, highlightthickness=0, cursor="hand2"
)
checkbutton.grid(row=row_counter, column=1, sticky="w", padx=10)
row_counter += 1

# --- Radiobuttons ---
Label(scrollable_frame, text="Radiobuttons:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
radio_frame = Frame(scrollable_frame, bg="white")
radio_frame.grid(row=row_counter, column=1, sticky="w")
radio_state = IntVar(value=1)
radiobutton1 = Radiobutton(
    radio_frame, text="Option 1", value=1, variable=radio_state, command=radio_used,
    font=widget_font, bg="white", fg="#0f172a", activebackground="white", activeforeground="#0f172a",
    selectcolor="#f1f5f9", relief=FLAT, bd=0, highlightthickness=0, cursor="hand2"
)
radiobutton2 = Radiobutton(
    radio_frame, text="Option 2", value=2, variable=radio_state, command=radio_used,
    font=widget_font, bg="white", fg="#0f172a", activebackground="white", activeforeground="#0f172a",
    selectcolor="#f1f5f9", relief=FLAT, bd=0, highlightthickness=0, cursor="hand2"
)
radiobutton1.pack(side=LEFT, padx=10)
radiobutton2.pack(side=LEFT)
row_counter += 1

# --- Listbox ---
Label(scrollable_frame, text="Listbox:", font=widget_font, bg="white", fg="#0f172a").grid(row=row_counter, column=0, sticky="w", pady=10)
listbox = Listbox(
    scrollable_frame, height=4, font=widget_font, fg="#0f172a", bg="#f1f5f9",
    relief=FLAT, bd=0, highlightthickness=0,
    selectbackground="#4f46e5", selectforeground="white"
)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(END, item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=row_counter, column=1, sticky="ew", padx=10)
row_counter += 1

# --- Start the GUI Main Loop ---
window.mainloop()
