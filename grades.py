class Grades:
    def __init__(self):
        self.grade_scale = {
            "A": (90, 100),
            "B": (80, 89),
            "C": (70, 79),
            "D": (60, 69),
            "F": (0, 59)
        }

    def display_grade_report(self):
        for grade, mark_range in self.grade_scale.items():
            print(f"{grade}: {mark_range[0]} - {mark_range[1]}")

    def add_grade(self, grade, low, high):
        self.grade_scale[grade] = (low, high)
        print("Grade added successfully.")

    def delete_grade(self, grade):
        if grade in self.grade_scale:
            del self.grade_scale[grade]
            print("Grade deleted successfully.")
            return True
        print("Grade not found.")
        return False

    def modify_grade(self, grade, low, high):
        if grade in self.grade_scale:
            self.grade_scale[grade] = (low, high)
            print("Grade updated successfully.")
            return True
        print("Grade not found.")
        return False

    def get_grade_from_marks(self, marks):
        for grade, mark_range in self.grade_scale.items():
            if mark_range[0] <= marks <= mark_range[1]:
                return grade
        return "Invalid"
