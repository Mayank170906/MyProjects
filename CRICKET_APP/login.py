import smtplib
import random
import sqlite3

class Signup:
    def __init__(self) -> None:
        self.name = None
        self.email = None
        self.password = None
        self.money = 0
        self.setup_database()

    def setup_database(self):
        # Connect to the SQLite database (or create it if it doesn't exist)
        self.conn = sqlite3.connect('user_data.db')
        self.cursor = self.conn.cursor()
        # Create table for users if it doesn't already exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                name TEXT,
                                email TEXT PRIMARY KEY,
                                password TEXT,
                                money INTEGER DEFAULT 0)''')
        self.conn.commit()

    def authentication(self):
        otp = random.randint(1000, 9999)

        FROM_MY = ".@yahoo.com"
        MY_PASSWORD = ""

        SEND_TO = input("Enter your email\n")

        SUBJ = "OTP FOR CRICY SIGNUP"

        MESSAGE = f"From:{FROM_MY}\nTo:{SEND_TO}\nSubject:{SUBJ}\n\nThe OTP for signup is {otp}"

        connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        connection.starttls()
        connection.login(FROM_MY, MY_PASSWORD)
        connection.sendmail(from_addr=FROM_MY, to_addrs=SEND_TO, msg=MESSAGE)

        for i in range(5):
            user = int(input("Enter the OTP\n"))
            if user == otp:
                print("OTP successfully verified")
                self.email = SEND_TO
                return True
            else:
                print("Incorrect OTP. Please try again.")
        return False

    def input_user_data(self):
        if self.authentication():
            self.name = input("Enter your name\n")
            self.password = input("Enter your password\n")
            self.money = 0
            # Store user data in the database
            self.cursor.execute("INSERT INTO users (name, email, password, money) VALUES (?, ?, ?, ?)",
                                (self.name, self.email, self.password, self.money))
            self.conn.commit()
            print("Details added successfully!")
            return True
        return False

    def add_money(self):
        add_money = int(input("Enter the amount you want to add: "))
        print("You are being redirected to another platform to complete the payment.")
        print("Payment successful.")
        self.money += add_money
        # Update money in the database
        self.cursor.execute("UPDATE users SET money = ? WHERE email = ?", (self.money, self.email))
        self.conn.commit()

    def withdraw_money(self):
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
        if withdraw_amount > self.money:
            print("Failed to withdraw. Please enter a lesser amount.")
            return
        print("You are being redirected to another platform to complete the payment.")
        print("Payment successful.")
        self.money -= withdraw_amount
        # Update money in the database
        self.cursor.execute("UPDATE users SET money = ? WHERE email = ?", (self.money, self.email))
        self.conn.commit()

    def login(self):
        email = input("Enter your email for login:\n")
        password = input("Enter your password:\n")
        # Query the database for the provided email and password
        self.cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cursor.fetchone()

        if user:
            self.name, self.email, self.password, self.money = user[1], user[2], user[3], user[4]  # Correct the unpacking
            print("Login successful!")
            return True
        else:
            print("Incorrect email or password.")
            return False
    def __del__(self):
        # Close the database connection when the object is destroyed
        self.conn.close()

    def delete_account(self):
        email = input("Enter your email to delete your account:\n")
        # Verify the user by email before deleting their account
        self.cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = self.cursor.fetchone()

        if user:
            confirm = input(f"Are you sure you want to delete the account associated with {email}? (yes/no): ")
            if confirm.lower() == "yes":
                self.cursor.execute("DELETE FROM users WHERE email = ?", (email,))
                self.conn.commit()
                print(f"Account associated with {email} has been deleted successfully.")
            else:
                print("Account deletion canceled.")
        else:
            print("Email not found in the system.")



# Instantiate and use the signup object
obj = Signup()
# if obj.input_user_data():
#     print("Proceeding to login...")
#     obj.login()
# obj.login()
obj.delete_account()
