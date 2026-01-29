import matplotlib.pyplot as plt

# ---------------- TIME COLUMN DETECTION ----------------
def detect_time_column(data):
    for col in ["Time", "Timestamp", "time", "timestamp"]:
        if col in data.columns:
            return col
    data["Time"] = range(len(data))
    return "Time"


# ---------------- CLEAN DATA UNTIL NULL ----------------
def clean_data_until_null(data, required_columns):
    for i, row in data.iterrows():
        if row[required_columns].isnull().any():
            return data.iloc[:i]
    return data


# ---------------- TEMPERATURE ANALYSIS ----------------
def plot_temperature(data):
    time_col = detect_time_column(data)
    data = clean_data_until_null(data, ["Sensor_Value", "Sensor_Status"])

    valid = data[data["Sensor_Status"] == "VALID"]
    error = data[data["Sensor_Status"] != "VALID"]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray")

    plt.scatter(valid[time_col], valid["Sensor_Value"], color="blue", label="VALID")
    plt.scatter(error[time_col], error["Sensor_Value"], color="red", label="ERROR")

    for _, row in error.iterrows():
        plt.text(row[time_col], row["Sensor_Value"] + 0.3,
                 "ERROR", color="red", ha="center")

    plt.title("Temperature Error Analysis")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Temperature Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------- FMI ANALYSIS ----------------
def plot_fmi(data):
    time_col = detect_time_column(data)
    data = clean_data_until_null(data, ["Sensor_Value", "Sensor_Status", "Index"])

    valid = data[data["Sensor_Status"] == "VALID"]
    error = data[data["Sensor_Status"] != "VALID"]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray")

    plt.scatter(valid[time_col], valid["Sensor_Value"], color="blue", label="VALID")
    plt.scatter(error[time_col], error["Sensor_Value"], color="red", label="ERROR")

    for _, row in error.iterrows():
        plt.text(row[time_col], row["Sensor_Value"] + 0.3,
                 f"ERROR | FMI {row['Index']}", color="red", ha="center")

    plt.title("FMI Diagnostic Analysis")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------- THRESHOLD ANALYSIS ----------------
def plot_custom_threshold(data, threshold):
    time_col = detect_time_column(data)
    data = clean_data_until_null(data, ["Sensor_Value"])

    normal = data[data["Sensor_Value"] <= threshold]
    fault = data[data["Sensor_Value"] > threshold]

    plt.figure(figsize=(10, 5))
    plt.plot(data[time_col], data["Sensor_Value"], "--", color="gray")

    plt.scatter(normal[time_col], normal["Sensor_Value"], color="blue", label="Below Threshold")
    plt.scatter(fault[time_col], fault["Sensor_Value"], color="red", label="Above Threshold")

    plt.axhline(threshold, linestyle="--", color="black", label="Threshold")

    plt.title("Threshold Analysis")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Sensor Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------- ROW-WISE ANALYSIS (DEFAULT = SENSOR_STATUS) ----------------
def plot_rowwise_parameter(data, parameter="Sensor_Status"):
    time_col = detect_time_column(data)
    data = clean_data_until_null(data, [parameter, "Sensor_Status"])

    plt.figure(figsize=(10, 5))

    # If Sensor_Status is selected (DEFAULT)
    if parameter == "Sensor_Status":
        valid = data[data["Sensor_Status"] == "VALID"]
        error = data[data["Sensor_Status"] != "VALID"]

        plt.scatter(valid[time_col], [1]*len(valid), color="blue", label="VALID")
        plt.scatter(error[time_col], [1]*len(error), color="red", label="ERROR")

        plt.yticks([1], ["Sensor Status"])
        plt.ylabel("Status")

    else:
        valid = data[data["Sensor_Status"] == "VALID"]
        error = data[data["Sensor_Status"] != "VALID"]

        plt.plot(data[time_col], data[parameter], "--", color="gray")
        plt.scatter(valid[time_col], valid[parameter], color="blue", label="VALID")
        plt.scatter(error[time_col], error[parameter], color="red", label="ERROR")

        for _, row in error.iterrows():
            plt.text(row[time_col], row[parameter] + 0.3,
                     "ERROR", color="red", ha="center")

        plt.ylabel(parameter)

    plt.title(f"Row-wise Analysis – {parameter}")
    plt.xlabel("Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
