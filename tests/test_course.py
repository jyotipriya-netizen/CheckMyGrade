import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from course import Course
from utils import write_csv


class TestCourse(unittest.TestCase):
    def setUp(self):
        self.course = Course()
        self.test_data = [
            {
                "course_id": "DATA200",
                "course_name": "Data Science",
                "credits": "3",
                "description": "Intro"
            }
        ]
        write_csv(self.course.FILE_PATH, self.test_data, self.course.HEADERS)

    def test_add_course(self):
        result = self.course.add_new_course("DATA201", "Statistics", 3, "Stats")
        self.assertTrue(result)

    def test_delete_course(self):
        result = self.course.delete_new_course("DATA200")
        self.assertTrue(result)

    def test_modify_course(self):
        result = self.course.modify_course("DATA200", course_name="Advanced Data Science")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
