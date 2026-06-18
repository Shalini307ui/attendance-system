# Smart Attendance Management System Using Face Recognition

##  Project Overview

The Smart Attendance Management System Using Face Recognition is a Python-based application that automates the attendance process using facial recognition technology.

The system recognizes registered users through a webcam, marks their attendance automatically, prevents duplicate entries, and exports attendance records to Excel format.

This project demonstrates the practical application of Computer Vision and Face Recognition in educational and organizational environments.

---

##  Features

- Real-time face recognition using webcam
-  Automatic attendance marking
-  Prevents duplicate attendance entries
-  Stores attendance records in CSV format
-  Exports attendance records to Excel (.xlsx)
-  Easy-to-use and efficient system
-  Can be extended with databases and dashboards

---

##  Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- Pandas
- OpenPyXL

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Shalini307ui/Attendance-System.git
```

### Navigate to the project folder

```bash
cd Attendance-System
```

### Install dependencies

```bash
pip install opencv-python
pip install face_recognition
pip install numpy
pip install pandas
pip install openpyxl
```

---

## How to Run

Run the following command:

```bash
python attendance.py
```

or

```bash
py attendance.py
```

---

##  How It Works

### Step 1: Load Registered Images

The system loads all images stored in the `image` folder.

Example:

```
img1.jpeg
img2.jpeg
img3.jpeg
```

---

### Step 2: Generate Face Encodings

Each registered face is converted into a numerical representation called a face encoding.

Example:

```
Person 1 → [0.12, -0.45, 0.67, ...]
Person 2 → [0.78, 0.11, -0.54, ...]
```

These encodings are stored for comparison.

---

### Step 3: Start Webcam

The webcam captures live video frames continuously.

---

### Step 4: Detect Faces

Faces present in the webcam feed are detected.

---

### Step 5: Compare Faces

The detected face is compared with the stored encodings.

If a match is found:

```
Face Recognized
       ↓
Display Name
       ↓
Mark Attendance
```

---

### Step 6: Record Attendance

Attendance is automatically saved in:

```
Attendance.csv
```

Example:

```
Name,Date,Time
IMG1,2026-06-18,09:30:15
IMG2,2026-06-18,09:35:40
```

---

### Step 7: Export to Excel

Attendance records are converted into:

```
Attendance.xlsx
```

This provides a professional attendance report that can be easily viewed and shared.

---

##  Project Workflow

```
Registered Images
       ↓
Face Encoding
       ↓
Webcam Input
       ↓
Face Detection
       ↓
Face Comparison
       ↓
Attendance Marking
       ↓
CSV Storage
       ↓
Excel Export
```

---

##  Applications

###  Educational Institutions
Automates classroom attendance and saves time.

###  Offices
Tracks employee attendance efficiently.

###  Libraries
Maintains entry and exit records.

###  Hostels
Monitors resident attendance.

###  Events and Conferences
Simplifies participant check-in.

---

##  Future Enhancements

- GUI using Tkinter
- SQLite Database Integration
- Email Notifications
- Attendance Analytics Dashboard
- QR Code Verification
- Unknown Face Alerts
- Multi-Camera Support

---

##  Skills Demonstrated

- Python Programming
- Computer Vision
- OpenCV
- Face Recognition
- Real-Time Processing
- File Handling
- Data Export using Pandas
- Problem Solving
- Git and GitHub

---

##  Author

**Shalini**

GitHub: https://github.com/Shalini307ui

---

## 📄 License

This project is intended for educational and learning purposes.

---

## ⭐ Support

If you found this project useful, please give it a Star ⭐ on GitHub.
