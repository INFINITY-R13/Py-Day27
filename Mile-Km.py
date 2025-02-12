import tkinter as tk

def convert():
    try:
        # Get the value from the entry widget and convert it to float
        miles = float(miles_entry.get())
        # Convert miles to kilometers (1 mile ≈ 1.60934 km)
        kilometers = miles * 1.60934
        # Update the result label with formatted output
        result_label.config(text=f"{miles} miles is equal to {kilometers:.2f} km")
    except ValueError:
        # In case of invalid input, display an error message
        result_label.config(text="Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Mile to KM Converter")
root.minsize(300, 150)

# Create and place a label for instructions
instruction_label = tk.Label(root, text="Enter distance in miles:")
instruction_label.pack(pady=5)

# Create and place an entry widget for user input
miles_entry = tk.Entry(root, width=20)
miles_entry.pack(pady=5)

# Create and place a button that triggers the conversion
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.pack(pady=5)

# Create and place a label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Start the GUI event loop
root.mainloop()
