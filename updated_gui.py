import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

from Updated_plot1 import (
    plot_temperature,
    plot_fmi,
    plot_custom_threshold,
    plot_rowwise_parameter
)

data = None

# ---------------- LOAD CSV ----------------
def browse_file():
    global data
    path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )
    if path:
        data = pd.read_csv(path, encoding="cp1252")
        data.columns = data.columns.str.strip()
        file_label.config(text=path.split("/")[-1])


# ---------------- DROPDOWN HANDLER ----------------
def on_option_change(*args):
    option = selected_option.get()

    threshold_label.pack_forget()
    threshold_entry.pack_forget()
    param_label.pack_forget()
    param_dropdown.pack_forget()

    if option == "Threshold Analysis":
        threshold_label.pack(pady=8)
        threshold_entry.pack()

    elif option == "Row-wise Analysis":
        param_var.set("Sensor_Status")   # ✅ DEFAULT PARAMETER
        param_label.pack(pady=8)
        param_dropdown.pack()


# ---------------- EXECUTE ----------------
def execute_plot():
    if data is None:
        messagebox.showerror("Error", "Please select a CSV file")
        return

    option = selected_option.get()

    if option == "Temperature":
        plot_temperature(data)

    elif option == "FMI":
        plot_fmi(data)

    elif option == "Threshold Analysis":
        plot_custom_threshold(data, float(threshold_entry.get()))

    elif option == "Row-wise Analysis":
        plot_rowwise_parameter(data, param_var.get())

    else:
        messagebox.showerror("Error", "Select an option")


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Ambient Sensor Diagnostic Tool")
root.geometry("820x540")

tk.Label(root, text="Ambient Sensor Diagnostic Tool",
         font=("Arial", 18, "bold")).pack(pady=20)

tk.Button(root, text="Browse CSV File",
          font=("Arial", 12), command=browse_file).pack(pady=10)

file_label = tk.Label(root, text="No file selected", font=("Arial", 10))
file_label.pack()

tk.Label(root, text="Select Parameter",
         font=("Arial", 12, "bold")).pack(pady=15)

selected_option = tk.StringVar(value="Select Option")
selected_option.trace_add("write", on_option_change)

tk.OptionMenu(
    root,
    selected_option,
    "Temperature",
    "FMI",
    "Threshold Analysis",
    "Row-wise Analysis"
).pack()

threshold_label = tk.Label(root, text="Enter Threshold Value")
threshold_entry = tk.Entry(root)

param_label = tk.Label(root, text="Select Data Parameter")
param_var = tk.StringVar(value="Sensor_Status")

param_dropdown = tk.OptionMenu(
    root,
    param_var,
    "Sensor_Status",
    "Sensor_Value",
    "Index"
)

tk.Button(root, text="Plot Selected Parameter",
          font=("Arial", 13, "bold"),
          bg="lightblue",
          command=execute_plot).pack(pady=30)

tk.Label(root,
         text="Note: Please save the plot image before closing the window.",
         font=("Arial", 9, "italic"),
         fg="gray").pack(side="bottom", pady=15)

root.mainloop()
