# student-attendence-system-project
import csv
from datetime import datetime

#load student from a file
def load_students(filename="students.csv"):
    students = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

#add new student
def add_student(filename="students.csv"):
    id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name])

    print(f"✅ Student '{name}' added successfully!")

#mark attendece for today
def mark_attendance(students, attendance_file="attendance.csv"):
    today = datetime.now().strftime("%Y-%m-%d")

    with open(attendance_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        for student in students:
            status = input(f"Is {student['Name']} present? (y/n): ").lower()
            attendance = 'Present' if status == 'y' else 'Absent'
            writer.writerow([today, student['ID'], student['Name'], attendance])
    
    print("✅ Attendance marked for today.")

#view all attendence records
def view_attendance(attendance_file="attendance.csv"):
    print("\n📋 Attendance Records:\n")
    with open(attendance_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

#view attendence bt date
def view_attendance_by_date(attendance_file="attendance.csv"):
    date = input("Enter date (YYYY-MM-DD): ")
    found = False
    with open(attendance_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == date:
                print(row)
                found = True
    if not found:
        print("❌ No records found for this date.")
        
#main menu logic
def main():
    while True:
        print("\n==== Student Attendance System ====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View All Attendance")
        print("4. View Attendance by Date")
        print("5. Exit")

        choice = input("Enter your choice: ")

        students = load_students()

        if choice == '1':
            add_student()
        elif choice == '2':
            mark_attendance(students)
        elif choice == '3':
            view_attendance()
        elif choice == '4':
            view_attendance_by_date()
        elif choice == '5':
            print("👋 Exiting system. Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()



