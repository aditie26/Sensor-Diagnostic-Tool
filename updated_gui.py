import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

from updated_plot import (
    plot_error,
    plot_fmi,
    plot_custom_threshold
)

data = None

# ---------------- FILE SELECTION ----------------
def browse_file():
    global data
    file_path = filedialog.askopenfilename(
        title="Select Ambient Sensor CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if file_path:
        try:
            data = pd.read_csv(file_path, encoding="cp1252")
            data.columns = data.columns.str.strip()
            file_label.config(text=file_path.split("/")[-1])
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ---------------- EXECUTE SELECTED OPTION ----------------
def execute_plot():
    if data is None:
        messagebox.showerror("Error", "Please select a CSV file")
        return

    option = selected_option.get()

    if option == "Error Plot":
        plot_error(data)

    elif option == "FMI Plot":
        plot_fmi(data)

    elif option == "Custom Threshold Plot":
        try:
            threshold = float(threshold_entry.get())
            plot_custom_threshold(data, threshold)
        except ValueError:
            messagebox.showerror("Error", "Enter valid threshold value")

    else:
        messagebox.showerror("Error", "Please select a parameter")


# ---------------- GUI WINDOW ----------------
root = tk.Tk()
root.title("Ambient Sensor Diagnostic Tool")
root.geometry("750x450")

tk.Label(root, text="Ambient Sensor Diagnostic Tool",
         font=("Arial", 18, "bold")).pack(pady=20)

tk.Button(root, text="Browse CSV File",
          font=("Arial", 12), command=browse_file).pack(pady=10)

file_label = tk.Label(root, text="No file selected", font=("Arial", 10))
file_label.pack()

# ---------------- DROPDOWN ----------------
tk.Label(root, text="Select Parameter",
         font=("Arial", 12, "bold")).pack(pady=15)

selected_option = tk.StringVar()
selected_option.set("Select Option")

dropdown = tk.OptionMenu(
    root,
    selected_option,
    "Error Plot",
    "FMI Plot",
    "Custom Threshold Plot"
)
dropdown.config(width=25, font=("Arial", 11))
dropdown.pack()

# ---------------- THRESHOLD ENTRY ----------------
tk.Label(root, text="Threshold Value (for Custom Threshold Plot)",
         font=("Arial", 10)).pack(pady=10)

threshold_entry = tk.Entry(root, width=15, font=("Arial", 11))
threshold_entry.pack()

# ---------------- PLOT BUTTON ----------------
tk.Button(
    root,
    text="Plot Selected Parameter",
    font=("Arial", 13, "bold"),
    bg="lightblue",
    command=execute_plot
).pack(pady=30)

root.mainloop()
