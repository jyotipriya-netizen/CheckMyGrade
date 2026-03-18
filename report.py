from student import Student
from professor import Professor


class Report:
    def __init__(self):
        self.student_obj = Student()
        self.professor_obj = Professor()

    def report_by_course(self, course_id):
        records = self.student_obj.generate_report_by_course(course_id)
        print(f"\nReport for Course: {course_id}")
        for record in records:
            print(record)

    def report_by_student(self, email_address):
        records = self.student_obj.generate_report_by_student(email_address)
        print(f"\nReport for Student: {email_address}")
        for record in records:
            print(record)

    def report_by_professor(self, professor_id):
        professor = self.professor_obj.show_course_details_by_professor(professor_id)
        if professor:
            course_id = professor["course_id"]
            print(f"\nReport for Professor: {professor['name']}")
            records = self.student_obj.generate_report_by_course(course_id)
            for record in records:
                print(record)
