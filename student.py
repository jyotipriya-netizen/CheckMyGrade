from utils import read_csv, write_csv, append_csv, search_with_time
import statistics


class Student:
    FILE_PATH = "data/students.csv"
    HEADERS = ["email_address", "first_name", "last_name", "course_id", "grade", "marks"]

    def display_records(self):
        students = read_csv(self.FILE_PATH)
        if not students:
            print("No student records found.")
            return
        for student in students:
            print(student)

    def add_new_student(self, email_address, first_name, last_name, course_id, grade, marks):
        students = read_csv(self.FILE_PATH)

        for student in students:
            if student["email_address"] == email_address:
                print("Student email must be unique.")
                return False

        new_student = {
            "email_address": email_address,
            "first_name": first_name,
            "last_name": last_name,
            "course_id": course_id,
            "grade": grade,
            "marks": str(marks)
        }

        append_csv(self.FILE_PATH, new_student, self.HEADERS)
        print("Student added successfully.")
        return True

    def delete_new_student(self, email_address):
        students = read_csv(self.FILE_PATH)
        updated_students = [student for student in students if student["email_address"] != email_address]

        if len(updated_students) == len(students):
            print("Student not found.")
            return False

        write_csv(self.FILE_PATH, updated_students, self.HEADERS)
        print("Student deleted successfully.")
        return True

    def update_student_record(self, email_address, **kwargs):
        students = read_csv(self.FILE_PATH)
        found = False

        for student in students:
            if student["email_address"] == email_address:
                for key, value in kwargs.items():
                    if key in student:
                        student[key] = str(value)
                found = True
                break

        if not found:
            print("Student not found.")
            return False

        write_csv(self.FILE_PATH, students, self.HEADERS)
        print("Student updated successfully.")
        return True

    def check_my_grades(self, email_address):
        students = read_csv(self.FILE_PATH)
        results, elapsed = search_with_time(students, "email_address", email_address)

        print(f"Search completed in {elapsed:.8f} seconds")
        if results:
            for result in results:
                print(f"{result['first_name']} {result['last_name']} - Grade: {result['grade']}")
        else:
            print("No student found.")

        return results, elapsed

    def check_my_marks(self, email_address):
        students = read_csv(self.FILE_PATH)
        results, elapsed = search_with_time(students, "email_address", email_address)

        print(f"Search completed in {elapsed:.8f} seconds")
        if results:
            for result in results:
                print(f"{result['first_name']} {result['last_name']} - Marks: {result['marks']}")
        else:
            print("No student found.")

        return results, elapsed

    def sort_records(self, field_name, reverse=False):
        students = read_csv(self.FILE_PATH)

        if field_name == "marks":
            sorted_students = sorted(students, key=lambda x: int(x["marks"]), reverse=reverse)
        else:
            sorted_students = sorted(students, key=lambda x: x[field_name].lower(), reverse=reverse)

        for student in sorted_students:
            print(student)

        return sorted_students

    def calculate_average_marks(self):
        students = read_csv(self.FILE_PATH)
        marks = [int(student["marks"]) for student in students]
        if not marks:
            return 0
        return sum(marks) / len(marks)

    def calculate_median_marks(self):
        students = read_csv(self.FILE_PATH)
        marks = [int(student["marks"]) for student in students]
        if not marks:
            return 0
        return statistics.median(marks)

    def generate_report_by_course(self, course_id):
        students = read_csv(self.FILE_PATH)
        report = [student for student in students if student["course_id"].lower() == course_id.lower()]
        return report

    def generate_report_by_student(self, email_address):
        students = read_csv(self.FILE_PATH)
        report = [student for student in students if student["email_address"].lower() == email_address.lower()]
        return report
