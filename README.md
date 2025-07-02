# 🎓 Student Management System (Tkinter Based)

This is a simple **Student Management System** built using **Python**, **Tkinter**, and **Matplotlib**, developed as a **first-year academic project**. It provides a basic GUI for **Admins**, **Students**, and **Teachers** to manage records, analyze data, and navigate role-based dashboards.

---

## 🧠 Key Features

- 🔐 **Login System** using `users.txt` and `password.txt`
- 🧑‍🏫 **Role-Based Dashboards**:
  - **Admin**: Add/view grades, manage users, visualize performance
  - **Teacher**: Access and update student records
  - **Student**: View grades, activities
- 📈 **Matplotlib-Based Visualizations**:
  - Grade distribution
  - Performance comparison charts
- 📁 **Flat-file Storage** using `.txt` files:
  - `users.txt` → list of usernames
  - `password.txt` → corresponding passwords
  - `grades.txt` → academic grades
  - `eca.txt` → extracurricular activity records
- 📊 GUI interface built using **Tkinter**
- 🧪 Sample data imported from **Kaggle**

---

## 📁 Project Structure

student-management-system/
├── tkinter2.py # All logic, GUI, and visualization in one file
├── users.txt # Demo user list (from Kaggle)
├── password.txt # Corresponding passwords
├── grades.txt # Grade records
├── eca.txt # Extra-curricular data
└── README.md


## 📦 Requirements

Install dependencies using:
pip install matplotlib
Tkinter is pre-installed with Python. You only need to install matplotlib if not already available.

💻 How to Run
python tkinter2.py

Use sample usernames and passwords from the users.txt and password.txt files.

📊 Visualizations
The system uses matplotlib to display:

Grade comparison

Extracurricular involvement

These charts help admins/teachers better understand student trends.

🛠️ Technologies Used
Python 

Tkinter (GUI)

Matplotlib (data visualization)

Text files (.txt) for persistent storage

Kaggle (sample data source)

⚙️ Notes
Built as a beginner-level academic project

Logic is consolidated in a single Python file for simplicity

Modularization or database integration can be added in future versions
