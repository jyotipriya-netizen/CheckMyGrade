from utils import read_csv, write_csv, append_csv


class Course:
    FILE_PATH = "data/courses.csv"
    HEADERS = ["course_id", "course_name", "credits", "description"]

    def display_courses(self):
        courses = read_csv(self.FILE_PATH)
        if not courses:
            print("No courses found.")
            return
        for course in courses:
            print(course)

    def add_new_course(self, course_id, course_name, credits, description):
        courses = read_csv(self.FILE_PATH)

        for course in courses:
            if course["course_id"] == course_id:
                print("Course ID must be unique.")
                return False

        new_course = {
            "course_id": course_id,
            "course_name": course_name,
            "credits": str(credits),
            "description": description
        }

        append_csv(self.FILE_PATH, new_course, self.HEADERS)
        print("Course added successfully.")
        return True

    def delete_new_course(self, course_id):
        courses = read_csv(self.FILE_PATH)
        updated_courses = [course for course in courses if course["course_id"] != course_id]

        if len(updated_courses) == len(courses):
            print("Course not found.")
            return False

        write_csv(self.FILE_PATH, updated_courses, self.HEADERS)
        print("Course deleted successfully.")
        return True

    def modify_course(self, course_id, **kwargs):
        courses = read_csv(self.FILE_PATH)
        found = False

        for course in courses:
            if course["course_id"] == course_id:
                for key, value in kwargs.items():
                    if key in course:
                        course[key] = str(value)
                found = True
                break

        if not found:
            print("Course not found.")
            return False

        write_csv(self.FILE_PATH, courses, self.HEADERS)
        print("Course updated successfully.")
        return True
