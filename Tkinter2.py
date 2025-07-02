import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variable to store the logged-in username
current_username = None

class User:
    def __init__(self, user_id, first_name, last_name, email, gender, phone, course, level, role):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.phone = phone
        self.course = course
        self.level = level
        self.role = role

    def __str__(self):
        return f"{self.user_id},{self.first_name},{self.last_name},{self.email},{self.gender},{self.phone},{self.course},{self.level},{self.role}\n"

class Admin(User):
    def __init__(self, user_id, first_name, last_name, email, gender, phone):
        super().__init__(user_id, first_name, last_name, email, gender, phone, "", "", "Admin")

class Student(User):
    def __init__(self, user_id, first_name, last_name, email, gender, phone, course, level):
        super().__init__(user_id, first_name, last_name, email, gender, phone, course, level, "Student")

class UserManager:
    @staticmethod
    def read_credentials_from_file(filename):
        credentials = {'admin': [], 'student': []}
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    user_id, username, password, role = parts
                    role = role.lower() if role.lower() in credentials else "admin"  # Set default role to admin if role not in credentials
                    credentials[role].append({'id': user_id, 'username': username, 'password': password.strip('"')})
                else:
                    print(f"Issue with line: {line.strip()}")  # Print problematic line for debugging
        return credentials
    @staticmethod
    def authenticate(window, username, password, role, credentials):
        for credential in credentials[role]:
            if credential["username"] == username and credential["password"] == password:
                messagebox.showinfo("Success", "Login successful!")
                window.destroy()
                if role == "admin":
                    AdminDashboard(username, UserManager.get_next_user_id).display_dashboard()
                else:
                    student_id = credential["id"]
                    StudentDashboard(student_id).display_dashboard()
                return credential["id"]  # Return the user ID
        messagebox.showerror("Error", "Invalid username or password.")

    @staticmethod
    def get_next_user_id():
        existing_ids = set()
        with open("users.txt", "r") as file:
            next(file)  # Skip the first line containing headers
            for line in file:
                parts = line.strip().split(",")
                user_id = parts[0]  # Assuming the user ID is the first column
                existing_ids.add(int(user_id))
        # Find the next available user ID
        return max(existing_ids) + 1 if existing_ids else 1


class AdminDashboard:

    def __init__(self, username, get_next_user_id):
        self.username = username
        self.get_next_user_id = get_next_user_id

    def display_dashboard(self):
            
        self.root = tk.Tk()
        self.root.title("Admin Dashboard")
        self.root.geometry("400x300")

        # Adding some styling
        self.root.config(bg="#ffffff")  # White background
        welcome_label = tk.Label(self.root, text="Welcome to the Admin Dashboard, " + self.username + "!", font=("Helvetica", 14), bg="#ffffff", fg="#333333")  # Dark gray text
        welcome_label.pack(pady=10)
        button_frame = tk.Frame(self.root, bg="#ffffff")  # Frame for buttons
        button_frame.pack()
        # Register Button
        register_button = tk.Button(button_frame, text="Register a new user", command=self.register_new_user, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")  # Green button with white text
        register_button.grid(row=0, column=0, padx=10, pady=5)
        # View Button
        view_button = tk.Button(button_frame, text="View users", command=self.view_users, font=("Helvetica", 12), bg="#FFC107", fg="#333333")  # Yellow button with dark gray text
        view_button.grid(row=0, column=1, padx=10, pady=5)
        # View ECA Records Button
        eca_button = tk.Button(button_frame, text="View ECA Records", command=self.view_eca_records, font=("Helvetica", 12), bg="#2196F3", fg="#ffffff")  # Blue button with white text
        eca_button.grid(row=1, column=0, padx=10, pady=5)
        # Edit Button
        edit_button = tk.Button(button_frame, text="Edit user information", command=self.edit_user_information, font=("Helvetica", 12), bg="#2196F3", fg="#ffffff")  # Blue button with white text
        edit_button.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
        # Logout Button
        logout_button = tk.Button(self.root, text="Logout", command=self.logout, font=("Helvetica", 12), bg="#FF5722", fg="#ffffff")  # Red button with white text
        logout_button.pack(pady=10)

        self.root.mainloop()

    def register_new_user(self):
        register_window = tk.Toplevel(self.root)
        register_window.title("Register New User")
        register_window.geometry("300x300")
        register_window.config(bg="#f0f0f0")

        first_name_label = tk.Label(register_window, text="Enter first name:", font=("Helvetica", 12), bg="#f0f0f0")
        first_name_label.pack()
        self.first_name_entry = tk.Entry(register_window, font=("Helvetica", 12))
        self.first_name_entry.pack()

        last_name_label = tk.Label(register_window, text="Enter last name:", font=("Helvetica", 12), bg="#f0f0f0")
        last_name_label.pack()
        self.last_name_entry = tk.Entry(register_window, font=("Helvetica", 12))
        self.last_name_entry.pack()

        email_label = tk.Label(register_window, text="Enter e-mail address:")
        email_label.pack()
        self.email_entry = tk.Entry(register_window)
        self.email_entry.pack()

        gender_label = tk.Label(register_window, text="Enter gender:")
        gender_label.pack()
        self.gender_entry = tk.Entry(register_window)
        self.gender_entry.pack()

        phone_label = tk.Label(register_window, text="Enter phone number:")
        phone_label.pack()
        self.phone_entry = tk.Entry(register_window)
        self.phone_entry.pack()

        role_label = tk.Label(register_window, text="Enter user's role (admin/student):")
        role_label.pack()
        self.role_entry = tk.Entry(register_window)
        self.role_entry.pack()

        course_label = tk.Label(register_window, text="Enter course:")
        course_label.pack()
        self.course_entry = tk.Entry(register_window)
        self.course_entry.pack()

        level_label = tk.Label(register_window, text="Enter level:")
        level_label.pack()
        self.level_entry = tk.Entry(register_window)
        self.level_entry.pack()

        register_button = tk.Button(register_window, text="Register", command=self.register_user, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
        register_button.pack(pady=10)

        back_to_dashboard_button = tk.Button(register_window, text="Back to Admin Dashboard", command=lambda: self.back_to_dashboard(register_window), font=("Helvetica", 12), bg="#2196F3", fg="#ffffff")
        back_to_dashboard_button.pack(pady=10)

    def register_user(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        role = self.role_entry.get()

         # Check if the role is Admin and course and level fields are filled
        if role == "Admin" and (course or level):
            messagebox.showerror("Invalid Input", "Admin users do not require course and level fields.")
            return

        # Check if the role is Student and course or level fields are empty
        if role == "Student" and (not course or not level):
            messagebox.showerror("Incomplete Input", "Student users require both course and level fields.")
            return


        if role == "Admin":
            new_user = Admin(UserManager.get_next_user_id(), first_name, last_name, email, gender, phone)
        elif role == "Student":
            course = self.course_entry.get()
            level = self.level_entry.get()
            new_user = Student(UserManager.get_next_user_id(), first_name, last_name, email, gender, phone, course, level)
        else:
            messagebox.showerror("Invalid Role", "Please enter a valid role (admin/student).")
            return  # Stop further execution if role is invalid

        
        with open("users.txt", "a") as file:
            file.write(str(new_user))

        messagebox.showinfo("Success", "User registration successful!")
        self.root.destroy()
        AdminDashboard(self.username, self.get_next_user_id).display_dashboard()

        
    def view_users(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Users")

        users_text = tk.Text(view_window)
        users_text.pack()

        with open("users.txt", "r") as file:
            for line in file:
                user = line.strip().split(",")
                role = user[-1]  # Extract the role of the user
                if role == "Admin":
                    # Print admin user information without course and level
                    users_text.insert(tk.END, f"ID: {user[0]}, First Name: {user[1]}, Last Name: {user[2]}, Email: {user[3]}, Gender: {user[4]}, Phone: {user[5]}, Role: {user[8]}\n")
                elif role == "Student":
                    # Print regular user information with course and level
                    users_text.insert(tk.END, f"ID: {user[0]}, First Name: {user[1]}, Last Name: {user[2]}, Email: {user[3]}, Gender: {user[4]}, Phone: {user[5]}, Course: {user[6]}, Level: {user[7]}, Role: {user[8]}\n")
                else:
                    # Print for other roles (if any)
                    users_text.insert(tk.END, line)

        search_button = tk.Button(view_window, text="Search", command=self.search_user)
        search_button.pack()


    def view_eca_records(self):
        eca_window = tk.Toplevel(self.root)
        eca_window.title("View ECA Records")
        eca_window.geometry("600x400")
        eca_window.config(bg="#ffffff")

        view_records_button = tk.Button(eca_window, text="View Records", command=self.view_records, font=("Helvetica", 12), bg="#FFC107", fg="#333333")
        view_records_button.pack(pady=10)

        view_chart_button = tk.Button(eca_window, text="View Pie Chart", command=self.view_eca_chart, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")
        view_chart_button.pack(pady=10)

        back_button = tk.Button(eca_window, text="Back to Admin Dashboard", command=eca_window.destroy, font=("Helvetica", 12), bg="#FF5722", fg="#ffffff")
        back_button.pack(pady=10)

    def view_records(self):
        eca_records_window = tk.Toplevel(self.root)
        eca_records_window.title("ECA Records")
        eca_records_window.geometry("600x400")
        eca_records_window.config(bg="#ffffff")

        eca_text = tk.Text(eca_records_window)
        eca_text.pack(fill="both", expand=True)

        with open("eca.txt", "r") as file:
            for line in file:
                eca_text.insert(tk.END, line)
        try:
            with open("eca.txt", "r") as file:
                for line in file:
                    eca_text.insert(tk.END, line)
        except FileNotFoundError:
            messagebox.showerror("Error", "ECA file not found.")



    def view_eca_chart(self):
        eca_chart_window = tk.Toplevel(self.root)
        eca_chart_window.title("ECA Pie Chart")
        eca_chart_window.geometry("800x400")
        eca_chart_window.config(bg="#ffffff")

        # Analyze and plot pie chart for sports data
        outdoor_sports_count = {}
        online_sports_count = {}

        with open("eca.txt", "r") as file:
            next(file)  # Skip the header
            for line in file:
                parts = line.strip().split(",")
                outdoor_sport = parts[3]
                online_sport = parts[4]
                if outdoor_sport:
                    if outdoor_sport in outdoor_sports_count:
                        outdoor_sports_count[outdoor_sport] += 1
                    else:
                        outdoor_sports_count[outdoor_sport] = 1
                if online_sport:
                    if online_sport in online_sports_count:
                        online_sports_count[online_sport] += 1
                    else:
                        online_sports_count[online_sport] = 1

        # Create figure and axes for the plot
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

        # Plot pie chart for outdoor sports
        ax1.pie(outdoor_sports_count.values(), labels=outdoor_sports_count.keys(), autopct='%1.1f%%', startangle=140)
        ax1.set_title("Outdoor Sports")
        ax1.axis('equal')

        # Plot pie chart for online sports
        ax2.pie(online_sports_count.values(), labels=online_sports_count.keys(), autopct='%1.1f%%', startangle=140)
        ax2.set_title("Online Sports")
        ax2.axis('equal')

        # Embed the plot into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=eca_chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


    def search_user(self):
        search_window = tk.Toplevel(self.root)
        search_window.title("Search User")

        search_label = tk.Label(search_window, text="Enter user ID or name to search:")
        search_label.pack()

        self.search_entry = tk.Entry(search_window)
        self.search_entry.pack()

        search_button = tk.Button(search_window, text="Search", command=self.search_user_action)
        search_button.pack()

    def search_user_action(self):
        search_criteria = self.search_entry.get()
        found = False
        with open("users.txt", "r") as file:
            for line in file:
                user = line.strip().split(",")
                if search_criteria == user[0] or search_criteria in (user[1], user[2]):  # Check ID, first name, or last name
                    found = True
                    result_window = tk.Toplevel(self.root)
                    result_window.title("Search Result")

                    user_label = tk.Label(result_window, text="User found:")
                    user_label.pack()

                    user_info_text = tk.Text(result_window)
                    user_info_text.pack()
                    user_info_text.insert(tk.END, line)
                    break
        if not found:
            messagebox.showinfo("Info", "User not found.")

    def edit_user_information(self):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit User Information")

        edit_label = tk.Label(edit_window, text="Select an option:")
        edit_label.pack()

        update_button = tk.Button(edit_window, text="Update user information", command=self.update_user_information)
        update_button.pack()

        delete_button = tk.Button(edit_window, text="Delete user", command=self.delete_user)
        delete_button.pack()

        return_button = tk.Button(edit_window, text="Return to main menu", command=edit_window.destroy)
        return_button.pack()

    def update_user_information(self):
        # Function to get user ID before showing update fields
        update_window = tk.Toplevel(self.root)
        update_window.title("Update User Information")

        user_id_label = tk.Label(update_window, text="Enter user ID to update information:")
        user_id_label.pack()

        self.user_id_entry = tk.Entry(update_window)
        self.user_id_entry.pack()

        update_button = tk.Button(update_window, text="OK", command=self.check_user_id)
        update_button.pack()

    def check_user_id(self):
        user_id = self.user_id_entry.get().strip()
        found = False
        with open("users.txt", "r") as file:
            for line in file:
                user_data = line.strip().split(",")
                if user_id == user_data[0]:
                    found = True
                    break
        if found:
            self.show_update_fields(user_id)
        else:
            messagebox.showinfo("Info", "User not found.")

    def show_update_fields(self, user_id):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update User Information")

        with open("users.txt", "r") as file:
            for line in file:
                user_data = line.strip().split(",")
                if user_id == user_data[0]:
                    break

        self.first_name_entry = tk.Entry(update_window)
        self.first_name_entry.insert(0, user_data[1])
        self.first_name_entry.pack()

        self.last_name_entry = tk.Entry(update_window)
        self.last_name_entry.insert(0, user_data[2])
        self.last_name_entry.pack()

        self.email_entry = tk.Entry(update_window)
        self.email_entry.insert(0, user_data[3])
        self.email_entry.pack()

        self.gender_entry = tk.Entry(update_window)
        self.gender_entry.insert(0, user_data[4])
        self.gender_entry.pack()

        self.phone_entry = tk.Entry(update_window)
        self.phone_entry.insert(0, user_data[5])
        self.phone_entry.pack()

        # Check if the user is an Admin or Student to decide whether to show course and level fields
        if user_data[-1] == "Admin":
            self.course_label = tk.Label(update_window, text="Admin users do not have course information")
            self.course_label.pack()
            self.level_label = tk.Label(update_window, text="Admin users do not have level information")
            self.level_label.pack()
        else:
            self.course_entry = tk.Entry(update_window)
            self.course_entry.insert(0, user_data[6] if len(user_data) > 6 else "")
            self.course_entry.pack()

            self.level_entry = tk.Entry(update_window)
            self.level_entry.insert(0, user_data[7] if len(user_data) > 7 else "")
            self.level_entry.pack()

        update_button = tk.Button(update_window, text="Update", command=lambda: self.update_user_action(update_window, user_id))
        update_button.pack()

    def update_user_action(self, update_window, user_id):
        updated_user = []

        with open("users.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                user = line.strip().split(",")
                if user_id == user[0]:
                    user[1] = self.first_name_entry.get()
                    user[2] = self.last_name_entry.get()
                    user[3] = self.email_entry.get()
                    user[4] = self.gender_entry.get()
                    user[5] = self.phone_entry.get()
                    if len(user) >= 7 and user[-1] != "Admin":  # Ensure it's not an Admin user
                        user[6] = self.course_entry.get()
                    if len(user) >= 8 and user[-1] != "Admin":  # Ensure it's not an Admin user
                        user[7] = self.level_entry.get()
                    updated_user = user
                    break

        if not updated_user:
            messagebox.showinfo("Info", "User not found.")
        else:
            messagebox.showinfo("Info", "User found. Updating information...")

            updated_info = "\n".join(["{}: {}".format(attr, value) for attr, value in zip(["First Name", "Last Name", "Email", "Gender", "Phone", "Course", "Level"], updated_user[1:])])

            with open("users.txt", "w") as file:
                for line in lines:
                    if line.strip().split(",")[0] == user_id:
                        file.write(",".join(updated_user) + "\n")
                    else:
                        file.write(line)

            messagebox.showinfo("Info", "User information updated.\n\n" + updated_info)

            # Ask if the admin wants to update more information
            update_more = messagebox.askquestion("Update More", "Do you want to update more user information?")
            if update_more == "yes":
                # Clear entry fields for next update
                for entry in [self.first_name_entry, self.last_name_entry, self.email_entry, self.gender_entry, self.phone_entry, self.course_entry, self.level_entry]:
                    entry.delete(0, tk.END)
            else:
                # Close update window and display the dashboard of edit information
                update_window.destroy()
                self.root.deiconify()  # Show the dashboard window again


    def delete_user(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete User")

        user_id_label = tk.Label(delete_window, text="Enter user ID to delete:")
        user_id_label.pack()
        self.delete_id_entry = tk.Entry(delete_window)
        self.delete_id_entry.pack()

        delete_button = tk.Button(delete_window, text="Delete", command=self.delete_user_action)
        delete_button.pack()

    def delete_user_action(self):
        user_id = self.delete_id_entry.get()
        found = False
        with open("users.txt", "r") as file:
            lines = file.readlines()
        with open("users.txt", "w") as file:
            for line in lines:
                user = line.strip().split(",")
                if user_id == user[0]:
                    found = True
                    print("\nUser found and deleted:")
                    print("ID\tFirst Name\tLast Name\tGender\tPhone\tCourse\tLevel\tRole")
                    print("\t".join(user))
                else:
                    file.write(line)
                
        if not found:
            messagebox.showinfo("Info", "User not found.")
        else:
            messagebox.showinfo("Info", "User found and deleted.")
            delete_more = messagebox.askquestion("Delete More", "Do you want to delete more user information?")
            if delete_more == "no":
                self.root.destroy()
                AdminDashboard(self.username, self.get_next_user_id).display_dashboard()
            else:
                self.delete_user()

    def back_to_dashboard(self, window):
        window.destroy()  # Destroy the current window
        self.root.deiconify()  # Show the admin dashboard window again

    def logout(self):
        self.root.destroy()  # Destroy the admin dashboard window
        create_login_window()

class StudentDashboard:
    def __init__(self, student_id):
        self.student_id = student_id

    def display_dashboard(self):
        self.root = tk.Tk()
        self.root.title("Student Dashboard")
        self.root.geometry("400x300")
        
        # Adding some styling
        self.root.config(bg="#ffffff")  # White background

        welcome_label = tk.Label(self.root, text="Welcome to the Student Dashboard, " , font=("Helvetica", 14), bg="#ffffff", fg="#333333")  # Dark gray text
        welcome_label.pack(pady=10)

        button_frame = tk.Frame(self.root, bg="#ffffff")  # Frame for buttons
        button_frame.pack()

        # View Grades Button
        view_grades_button = tk.Button(button_frame, text="View Grades", command=self.view_grades, font=("Helvetica", 12), bg="#4CAF50", fg="#ffffff")  # Green button with white text
        view_grades_button.grid(row=0, column=0, padx=10, pady=5)

        # View ECA Record Button
        view_eca_button = tk.Button(button_frame, text="View ECA Record", command=self.view_eca_record, font=("Helvetica", 12), bg="#FFC107", fg="#333333")  # Yellow button with dark gray text
        view_eca_button.grid(row=0, column=1, padx=10, pady=5)

        # Logout Button
        logout_button = tk.Button(self.root, text="Logout", command=self.logout, font=("Helvetica", 12), bg="#FF5722", fg="#ffffff")  # Red button with white text
        logout_button.pack(pady=10)

        self.root.mainloop()

    def view_grades(self):
        self.root.withdraw()  # Hide the student dashboard window
        grades_window = tk.Toplevel(self.root)
        grades_window.title("Grades")
        grades_window.geometry("600x400")

        headers = ["ID", "First Name", "Last Name", "IT", "FOD", "English", "FOM"]
        for i, header in enumerate(headers):
            header_label = tk.Label(grades_window, text=header, font=("Helvetica", 12, "bold"))
            header_label.grid(row=0, column=i, padx=5, pady=5)
    
        try:
            with open("grades.txt", "r") as file:
                for idx, line in enumerate(file):
                    parts = line.strip().split(",")
                    if parts[0] == self.student_id:
                        for i, part in enumerate(parts):
                            grade_label = tk.Label(grades_window, text=part, font=("Helvetica", 12))
                            grade_label.grid(row=idx+1, column=i, padx=5, pady=5)  # Adjust row index to start from 1
                    else:
                         print(f"Issue with line: {line.strip()}")
        except FileNotFoundError:
            messagebox.showerror("Error", "Grades file not found.")
        
        # Button to go back to student dashboard
        back_button = tk.Button(grades_window, text="Back to Dashboard", command=lambda: self.back_to_dashboard(grades_window), font=("Helvetica", 12))
        back_button.grid(row=idx+1, columnspan=7, padx=5, pady=10)


    def view_eca_record(self):
        self.root.withdraw()  # Hide the student dashboard window
        eca_window = tk.Toplevel(self.root)
        eca_window.title("ECA Record")
        eca_window.geometry("600x400")
    
        headers = ["ID", "First Name", "Last Name", "Outdoor Sports", "Online Sports"]
        for i, header in enumerate(headers):
            header_label = tk.Label(eca_window, text=header, font=("Helvetica", 12, "bold"))
            header_label.grid(row=0, column=i, padx=5, pady=5)
        
        # Read ECA records from file
        try:
            with open("eca.txt", "r") as file:
                for idx, line in enumerate(file):
                    parts = line.strip().split(",")
                    if parts[0] == self.student_id:
                        for i, part in enumerate(parts):
                            eca_label = tk.Label(eca_window, text=part, font=("Helvetica", 12))
                            eca_label.grid(row=idx+1, column=i, padx=5, pady=5)  # Adjust row index to start from 1
                    else:
                        print(f"Issue with line: {line.strip()}")
        except FileNotFoundError:
            messagebox.showerror("Error", "ECA file not found.")
    
        # Button to go back to student dashboard
        back_button = tk.Button(eca_window, text="Back to Dashboard", command=lambda: self.back_to_dashboard(eca_window), font=("Helvetica", 12))
        back_button.grid(row=idx+1, columnspan=5, padx=5, pady=10)
    
    def back_to_dashboard(self, window):
        window.destroy()  # Destroy the current window
        self.root.deiconify()  # Show the student dashboard window again

    def logout(self):
        self.root.destroy()  # Destroy the student dashboard window
        create_login_window()

def create_login_window():
    login_window = tk.Tk()
    login_window.title("Login")
    login_window.geometry("300x250")

    username_label = tk.Label(login_window, text="Username:", font=("Helvetica", 12), bg="#ffffff")
    username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    username_entry = tk.Entry(login_window, font=("Helvetica", 12))
    username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    password_label = tk.Label(login_window, text="Password:", font=("Helvetica", 12), bg="#ffffff")
    password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    password_entry = tk.Entry(login_window, show="*", font=("Helvetica", 12))
    password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

    role_label = tk.Label(login_window, text="Select Role:", font=("Helvetica", 12), bg="#ffffff")
    role_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    role_var = tk.StringVar(login_window)
    role_var.set("admin")  # Default role is admin
    role_dropdown = tk.OptionMenu(login_window, role_var, "admin", "student")
    role_dropdown.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

    # Load and display login button image
    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 12), command=lambda: UserManager.authenticate(login_window, username_entry.get(), password_entry.get(), role_var.get(), credentials))
    login_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


    login_window.mainloop()
if __name__ == "__main__":
    print("Welcome to the program!")

    # Read credentials from password.txt file
    credentials = UserManager.read_credentials_from_file("password.txt")

    # Start the login process
    create_login_window()
