```python
import sqlite3
from sqlite3 import Error
import getpass
import os

class StudentManagementSystem:
    def __init__(self, db_name):
        self.conn = None
        try:
            # Connect to SQLite database. If it does not exist then it will be created.
            self.conn = sqlite3.connect(db_name)
            print(f"Connected to SQLite Database")
        except Error as e:
            print(e)

    def create_table(self):
        sql_create_students_table = """ CREATE TABLE IF NOT EXISTS students (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        first_name text NOT NULL,
                                        last_name text NOT NULL,
                                        email text UNIQUE NOT NULL,
                                        phone_number text NOT NULL
                                    ); """
        
        try:
            self.conn.execute(sql_create_students_table)
            print("Table created successfully")
        except Error as e:
            print(e)

    def create_student(self, first_name, last_name, email, phone_number):
        sql_create_student = """ INSERT INTO students (first_name, last_name, email, phone_number)
                                VALUES (?, ?, ?, ?) """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_create_student, (first_name, last_name, email, phone_number))
            print(f"Student {email} created successfully")
            self.conn.commit()
        except Error as e:
            print(e)

    def update_student(self, id, first_name=None, last_name=None, email=None, phone_number=None):
        sql_update_student = """ UPDATE students
                                SET first_name = ?, last_name = ?, email = ?, phone_number = ?
                                WHERE id = ? """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_update_student, (first_name, last_name, email, phone_number, id))
            print(f"Student {id} updated successfully")
            self.conn.commit()
        except Error as e:
            print(e)

    def delete_student(self, id):
        sql_delete_student = """ DELETE FROM students
                                WHERE id = ? """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_delete_student, (id,))
            print(f"Student {id} deleted successfully")
            self.conn.commit()
        except Error as e:
            print(e)

    def display_students(self):
        sql_select_all_students = """ SELECT * FROM students """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_select_all_students)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
            print("Students display completed")
        except Error as e:
            print(e)

    def login(self, email, password):
        sql_login = """ SELECT * FROM students
                       WHERE email = ? AND password = ?
                       """
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_login, (email, password))
            row = cursor.fetchone()
            if row is not None and row[2] == password:
                print(f"Login successful for {email}")
                return True
            else:
                print("Incorrect email or password")
                return False
        except Error as e:
            print(e)

def main():
    db_name = "students.db"
    
    if os.path.exists(db_name):
        os.remove(db_name)
        
    sms = StudentManagementSystem(db_name)
    while True:
        print("1. Create Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Display Students")
        print("5. Login")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            phone_number = input("Enter Phone Number: ")
            sms.create_student(first_name, last_name, email, phone_number)
        elif choice == "2":
            id = int(input("Enter Student ID: "))
            first_name = input("Enter First Name (Press Enter to skip): ")
            if first_name:
                first_name = first_name
            else:
                first_name = None
            last_name = input("Enter Last Name (Press Enter to skip): ")
            if last_name:
                last_name = last_name
            else:
                last_name = None
            email = input("Enter Email (Press Enter to skip): ")
            if email:
                email = email
            else:
                email = None
            phone_number = input("Enter Phone Number (Press Enter to skip): ")
            if phone_number:
                phone_number = phone_number
            else:
                phone_number = None
            sms.update_student(id, first_name, last_name, email, phone_number)
        elif choice == "3":
            id = int(input("Enter Student ID: "))
            sms.delete_student(id)
        elif choice == "4":
            sms.display_students()
        elif choice == "5":
            email = input("Enter Email: ")
            password = getpass.getpass("Enter Password: ")
            sms.login(email, password)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```