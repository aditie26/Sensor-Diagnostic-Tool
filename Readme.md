Ambient Sensor Diagnostic Tool
📌 Project Overview

The Ambient Sensor Diagnostic Tool is a Python-based GUI application developed to analyze mentor-provided ambient sensor data.
The tool enables engineers to visualize sensor behavior, detect error conditions, display FMI (Failure Mode Identifier) indices, and perform custom threshold-based analysis through an interactive graphical interface.

This project aligns with industrial diagnostic and software testing practices.

🎯 Objectives

Analyze ambient sensor data provided in CSV format

Identify and visualize error conditions

Display FMI indices for diagnostic understanding

Allow user-defined threshold testing

Provide a simple and interactive GUI for analysis

🛠 Technologies Used

Python 3.x

Pandas – Data handling and preprocessing

Matplotlib – Data visualization

Tkinter – Graphical User Interface (GUI)

📂 Project Structure
sensor_data_project/
│
├── data/
│   └── ambient_sensor_data.csv
│
├── scripts/
│   ├── ambient_sensor_gui.py
│   ├── ambient_sensor_plots.py
│
├── README.md

🖥 GUI Features

Browse and select CSV files from any directory

Dropdown selection (Select Parameter) with three options:

Error Plot

FMI Plot

Custom Threshold Plot

User-defined threshold input

One-click plot generation

📈 Plot Descriptions
🔴 Error Plot

Blue dots → Normal sensor values

Red dots → Error conditions

Each error point is labeled as ERROR

🔵 FMI Plot

Blue dots → Normal sensor values

Red dots → Error conditions

Each error point displays ERROR | FMI Index

⚙ Custom Threshold Plot

User-defined threshold line

Values exceeding the threshold are highlighted as faults

▶ How to Run the Project
1️⃣ Install Required Libraries
pip install pandas matplotlib

2️⃣ Navigate to Scripts Folder
cd sensor_data_project/scripts

3️⃣ Run the GUI
python ambient_sensor_gui.py

🏭 Industrial Relevance

Supports diagnostic analysis and fault visualization

Useful for Software-in-the-Loop (SIL) testing

Reduces manual sensor log inspection

Helps identify failure modes using FMI

🚀 Future Enhancements

Real-time sensor data integration

Automated fault summary reports

Multiple sensor comparison

Predictive fault detection using Machine Learning

Export plots directly from GUI

👩‍💻 Author

Aditi Joshi
Electronics & Telecommunication Engineering
Intern – Cummins India Pvt. Ltd.

📌 Conclusion

This project demonstrates a practical, GUI-based approach for analyzing ambient sensor diagnostics using real-world data.
It effectively combines visualization, error detection, and diagnostic indexing in a user-friendly tool suitable for industrial environments.