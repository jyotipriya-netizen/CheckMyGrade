import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from professor import Professor
from utils import write_csv


class TestProfessor(unittest.TestCase):
    def setUp(self):
        self.professor = Professor()
        self.test_data = [
            {
                "professor_id": "P101",
                "name": "Micheal John",
                "email_address": "micheal@mycsu.edu",
                "rank": "Senior Professor",
                "course_id": "DATA200"
            }
        ]
        write_csv(self.professor.FILE_PATH, self.test_data, self.professor.HEADERS)

    def test_add_professor(self):
        result = self.professor.add_new_professor("P102", "Sarah Lee", "sarah@mycsu.edu", "Assistant", "DATA201")
        self.assertTrue(result)

    def test_delete_professor(self):
        result = self.professor.delete_professor("P101")
        self.assertTrue(result)

    def test_modify_professor(self):
        result = self.professor.modify_professor_details("P101", rank="Lead Professor")
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
