import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from student import Student
from utils import write_csv


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student()
        self.test_data = [
            {
                "email_address": "a@test.com",
                "first_name": "A",
                "last_name": "One",
                "course_id": "DATA200",
                "grade": "A",
                "marks": "95"
            },
            {
                "email_address": "b@test.com",
                "first_name": "B",
                "last_name": "Two",
                "course_id": "DATA201",
                "grade": "B",
                "marks": "85"
            }
        ]
        write_csv(self.student.FILE_PATH, self.test_data, self.student.HEADERS)

    def test_add_student(self):
        result = self.student.add_new_student("c@test.com", "C", "Three", "DATA200", "A", 91)
        self.assertTrue(result)

    def test_delete_student(self):
        result = self.student.delete_new_student("a@test.com")
        self.assertTrue(result)

    def test_update_student(self):
        result = self.student.update_student_record("a@test.com", first_name="Updated")
        self.assertTrue(result)

    def test_sort_by_marks(self):
        result = self.student.sort_records("marks")
        self.assertEqual(result[0]["email_address"], "b@test.com")

    def test_average_marks(self):
        avg = self.student.calculate_average_marks()
        self.assertEqual(avg, 90.0)

    def test_median_marks(self):
        median = self.student.calculate_median_marks()
        self.assertEqual(median, 90.0)


if __name__ == "__main__":
    unittest.main()
