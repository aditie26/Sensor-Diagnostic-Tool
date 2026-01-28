import matplotlib.pyplot as plt

# ---------------- TIME COLUMN DETECTION ----------------
def detect_time_column(data):
    for col in ["Time", "Timestamp", "time", "timestamp"]:
        if col in data.columns:
            return col
    data["Time"] = range(len(data))
    return "Time"


# ---------------- ERROR PLOT ----------------
def plot_error(data):
    time_col = detect_time_column(data)

    normal = data[data["Sensor_Status"] == "VALID"]
    error = data[data["Sensor_Status"] != "VALID"]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray", label="Sensor Trend")

    plt.scatter(normal[time_col], normal["Sensor_Value"], color="blue", label="Status_Valid")
    plt.scatter(error[time_col], error["Sensor_Value"], color="red", label="Status_Error")

    for _, row in error.iterrows():
        plt.text(row[time_col], row["Sensor_Value"] + 0.3, "ERROR",
                 fontsize=9, color="red", ha="center")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.title("Ambient Sensor – Error Plot")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------- FMI PLOT ----------------
def plot_fmi(data):
    time_col = detect_time_column(data)

    normal = data[data["Sensor_Status"] == "VALID"]
    error = data[data["Sensor_Status"] != "VALID"]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray", label="Sensor Trend")

    plt.scatter(normal[time_col], normal["Sensor_Value"], color="blue", label="Normal")
    plt.scatter(error[time_col], error["Sensor_Value"], color="red", label="Error")

    for _, row in error.iterrows():
        plt.text(row[time_col], row["Sensor_Value"] + 0.3,
                 f"ERROR | FMI {row['Index']}",
                 fontsize=9, color="red", ha="center")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.title("Ambient Sensor – FMI Plot")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------- CUSTOM THRESHOLD PLOT ----------------
def plot_custom_threshold(data, threshold):
    time_col = detect_time_column(data)

    normal = data[data["Sensor_Value"] <= threshold]
    fault = data[data["Sensor_Value"] > threshold]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray", label="Sensor Trend")

    plt.scatter(normal[time_col], normal["Sensor_Value"], color="blue", label="Below Threshold")
    plt.scatter(fault[time_col], fault["Sensor_Value"], color="red", label="Above Threshold")

    plt.axhline(y=threshold, color="black", linestyle="--", label="Threshold")

    for _, row in fault.iterrows():
        plt.text(row[time_col], row["Sensor_Value"] + 0.3,
                 "THRESHOLD FAULT", fontsize=9, color="red", ha="center")

    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.title("Ambient Sensor – Custom Threshold Plot")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
