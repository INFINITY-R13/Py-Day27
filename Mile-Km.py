# Mile-Km.py

# Import the tkinter library, using 'tk' as an alias for convenience.
import tkinter as tk

def convert():
    """
    This function is called when the 'Convert' button is clicked.
    It reads the value from the miles entry, converts it to kilometers,
    and updates the result label. It also handles invalid input.
    """
    try:
        # Get the string from the entry widget and convert it to a floating-point number.
        miles = float(miles_entry.get())
        
        # The conversion factor for miles to kilometers.
        kilometers = miles * 1.60934
        
        # Update the result_label's text to show the conversion.
        # The f-string formats the output to two decimal places (.2f).
        result_label.config(text=f"{miles} miles is equal to {kilometers:.2f} km")
        
    except ValueError:
        # If float() fails (e.g., user entered "abc"), a ValueError occurs.
        # This block catches the error and displays a user-friendly message.
        result_label.config(text="Please enter a valid number.")

# --- Create the main window ---
root = tk.Tk()
root.title("Mile to KM Converter")
root.minsize(300, 150)
# Add some padding to the window for better spacing.
root.config(padx=20, pady=20)


# --- Create and place widgets ---

# Create and place a label for instructions.
instruction_label = tk.Label(root, text="Enter distance in miles:")
instruction_label.pack(pady=5) # .pack() is a simple layout manager. pady adds vertical padding.

# Create and place an entry widget for user input.
miles_entry = tk.Entry(root, width=20)
miles_entry.pack(pady=5)

# Create and place a button that triggers the 'convert' function.
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=5)

# Create and place a label to display the result. Initially, it's empty.
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# --- Start the GUI event loop ---
# This keeps the window open and responsive to user actions.
root.mainloop()