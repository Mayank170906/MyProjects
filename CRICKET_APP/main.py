import tkinter as tk
from tkinter import messagebox
import smtplib
import random
import sqlite3
from tkinter import simpledialog


class Signup:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None
        self.money = 0
        self.setup_database()

    def setup_database(self):
        self.conn = sqlite3.connect('user_data.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                name TEXT,
                                email TEXT PRIMARY KEY,
                                password TEXT,
                                money INTEGER DEFAULT 0)''')
        self.conn.commit()

    def send_otp(self, email):
        otp = random.randint(1000, 9999)
        FROM_MY = "mayankeducation.17@yahoo.com"
        MY_PASSWORD = "mnpdkbeyfrmosllo"
        SUBJ = "OTP FOR CRICY"
        MESSAGE = f"From:{FROM_MY}\nTo:{email}\nSubject:{SUBJ}\n\nThe OTP for verification is {otp}"

        try:
            connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
            connection.starttls()
            connection.login(FROM_MY, MY_PASSWORD)
            connection.sendmail(from_addr=FROM_MY, to_addrs=email, msg=MESSAGE)
            connection.quit()
            return otp
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send OTP: {e}")
            return None

    def authenticate_email(self, email):
        otp = self.send_otp(email)
        if otp is None:
            return False
        for _ in range(5):
            user_otp = simpledialog.askinteger("OTP Verification", "Enter the OTP sent to your email:")
            if user_otp == otp:
                messagebox.showinfo("Success", "OTP verified successfully!")
                return True
            else:
                messagebox.showerror("Error", "Incorrect OTP. Try again.")
        return False

    def login(self, email, password):
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()
        return user

    def signup(self, name, email, password):
        try:
            self.cursor.execute("INSERT INTO users (name, email, password, money) VALUES (?, ?, ?, ?)",
                                (name, email, password, 0))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def reset_password(self, email, new_password):
        self.cursor.execute("UPDATE users SET password = ? WHERE email = ?", (new_password, email))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cricy Login Page")
        self.signup_manager = Signup()
        self.create_login_page()

    def create_login_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Cricy Login", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Signup", command=self.create_signup_page).pack(pady=5)
        tk.Button(self.root, text="Forgot Password", command=self.forgot_password).pack(pady=5)

    def create_signup_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Cricy Signup", font=("Arial", 20)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack()

        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack()

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*", width=30)
        self.password_entry.pack()

        tk.Button(self.root, text="Register", command=self.signup).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.create_login_page).pack(pady=5)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user = self.signup_manager.login(email, password)
        if user:
            messagebox.showinfo("Success", f"Welcome back, {user[0]}!")
        else:
            messagebox.showerror("Error", "Invalid email or password.")

    def signup(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if self.signup_manager.authenticate_email(email):
            if self.signup_manager.signup(name, email, password):
                messagebox.showinfo("Success", "Account created successfully!")
                self.create_login_page()
            else:
                messagebox.showerror("Error", "Email already registered.")

    def forgot_password(self):
        email = tk.simpledialog.askstring("Forgot Password", "Enter your registered email:")
        if email:
            if self.signup_manager.authenticate_email(email):
                new_password = tk.simpledialog.askstring("Reset Password", "Enter your new password:", show="*")
                if new_password:
                    self.signup_manager.reset_password(email, new_password)
                    messagebox.showinfo("Success", "Password reset successfully!")
                else:
                    messagebox.showerror("Error", "Password cannot be empty.")
            else:
                messagebox.showerror("Error", "Failed to verify email.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
