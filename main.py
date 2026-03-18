from student import Student
from course import Course
from professor import Professor
from grades import Grades
from login_user import LoginUser
from report import Report


student_obj = Student()
course_obj = Course()
professor_obj = Professor()
grade_obj = Grades()
login_obj = LoginUser()
report_obj = Report()

def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. Display Students")
        print("2. Add Student")
        print("3. Delete Student")
        print("4. Update Student")
        print("5. Search Grade by Email")
        print("6. Search Marks by Email")
        print("7. Sort by Marks Ascending")
        print("8. Sort by Marks Descending")
        print("9. Sort by Email Ascending")
        print("10. Show Average Marks")
        print("11. Show Median Marks")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_obj.display_records()

        elif choice == "2":
            email = input("Email: ")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            cid = input("Course ID: ")
            marks = int(input("Marks: "))
            grade = grade_obj.get_grade_from_marks(marks)
            student_obj.add_new_student(email, fname, lname, cid, grade, marks)

        elif choice == "3":
            email = input("Enter student email to delete: ")
            student_obj.delete_new_student(email)

        elif choice == "4":
            email = input("Enter email of student to update: ")
            field = input("Enter field to update (first_name, last_name, course_id, marks, grade): ")
            value = input("Enter new value: ")
            if field == "marks":
                value = int(value)
            student_obj.update_student_record(email, **{field: value})

        elif choice == "5":
            email = input("Enter student email: ")
            student_obj.check_my_grades(email)

        elif choice == "6":
            email = input("Enter student email: ")
            student_obj.check_my_marks(email)

        elif choice == "7":
            student_obj.sort_records("marks", reverse=False)

        elif choice == "8":
            student_obj.sort_records("marks", reverse=True)

        elif choice == "9":
            student_obj.sort_records("email_address", reverse=False)

        elif choice == "10":
            avg = student_obj.calculate_average_marks()
            print(f"Average Marks: {avg:.2f}")

        elif choice == "11":
            median = student_obj.calculate_median_marks()
            print(f"Median Marks: {median}")

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def course_menu():
    while True:
        print("\n--- Course Menu ---")
        print("1. Display Courses")
        print("2. Add Course")
        print("3. Delete Course")
        print("4. Modify Course")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            course_obj.display_courses()

        elif choice == "2":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            credits = input("Credits: ")
            desc = input("Description: ")
            course_obj.add_new_course(cid, cname, credits, desc)

        elif choice == "3":
            cid = input("Enter course ID to delete: ")
            course_obj.delete_new_course(cid)

        elif choice == "4":
            cid = input("Enter course ID to modify: ")
            field = input("Enter field to update (course_name, credits, description): ")
            value = input("Enter new value: ")
            course_obj.modify_course(cid, **{field: value})

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def professor_menu():
    while True:
        print("\n--- Professor Menu ---")
        print("1. Display Professors")
        print("2. Add Professor")
        print("3. Delete Professor")
        print("4. Modify Professor")
        print("5. Show Course by Professor")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            professor_obj.professors_details()

        elif choice == "2":
            pid = input("Professor ID: ")
            name = input("Name: ")
            email = input("Email Address: ")
            rank = input("Rank: ")
            cid = input("Course ID: ")
            professor_obj.add_new_professor(pid, name, email, rank, cid)

        elif choice == "3":
            pid = input("Enter professor ID to delete: ")
            professor_obj.delete_professor(pid)

        elif choice == "4":
            pid = input("Enter professor ID to modify: ")
            field = input("Enter field to update (name, email_address, rank, course_id): ")
            value = input("Enter new value: ")
            professor_obj.modify_professor_details(pid, **{field: value})

        elif choice == "5":
            pid = input("Enter professor ID: ")
            professor_obj.show_course_details_by_professor(pid)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def login_menu():
    while True:
        print("\n--- Login Menu ---")
        print("1. Register User")
        print("2. Login")
        print("3. Change Password")
        print("4. Logout")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_id = input("User Email: ")
            password = input("Password: ")
            role = input("Role: ")
            login_obj.register_user(user_id, password, role)

        elif choice == "2":
            user_id = input("User Email: ")
            password = input("Password: ")
            login_obj.login(user_id, password)

        elif choice == "3":
            user_id = input("User Email: ")
            new_password = input("New Password: ")
            login_obj.change_password(user_id, new_password)

        elif choice == "4":
            login_obj.logout()

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def report_menu():
    while True:
        print("\n--- Report Menu ---")
        print("1. Report by Course")
        print("2. Report by Student")
        print("3. Report by Professor")
        print("0. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            course_id = input("Enter Course ID: ")
            report_obj.report_by_course(course_id)

        elif choice == "2":
            email = input("Enter Student Email: ")
            report_obj.report_by_student(email)

        elif choice == "3":
            professor_id = input("Enter Professor ID: ")
            report_obj.report_by_professor(professor_id)

        elif choice == "0":
            break

        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n====== CheckMyGrade Application ======")
        print("1. Student Operations")
        print("2. Course Operations")
        print("3. Professor Operations")
        print("4. Grade Operations")
        print("5. Login Operations")
        print("6. Reports")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_menu()
        elif choice == "2":
            course_menu()
        elif choice == "3":
            professor_menu()
        elif choice == "4":
            grade_obj.display_grade_report()
        elif choice == "5":
            login_menu()
        elif choice == "6":
            report_menu()
        elif choice == "0":
            print("Exiting application...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
