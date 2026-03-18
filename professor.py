from utils import read_csv, write_csv, append_csv


class Professor:
    FILE_PATH = "data/professors.csv"
    HEADERS = ["professor_id", "name", "email_address", "rank", "course_id"]

    def professors_details(self):
        professors = read_csv(self.FILE_PATH)
        if not professors:
            print("No professor records found.")
            return
        for professor in professors:
            print(professor)

    def add_new_professor(self, professor_id, name, email_address, rank, course_id):
        professors = read_csv(self.FILE_PATH)

        for professor in professors:
            if professor["professor_id"] == professor_id:
                print("Professor ID must be unique.")
                return False

        new_professor = {
            "professor_id": professor_id,
            "name": name,
            "email_address": email_address,
            "rank": rank,
            "course_id": course_id
        }

        append_csv(self.FILE_PATH, new_professor, self.HEADERS)
        print("Professor added successfully.")
        return True

    def delete_professor(self, professor_id):
        professors = read_csv(self.FILE_PATH)
        updated_professors = [professor for professor in professors if professor["professor_id"] != professor_id]

        if len(updated_professors) == len(professors):
            print("Professor not found.")
            return False

        write_csv(self.FILE_PATH, updated_professors, self.HEADERS)
        print("Professor deleted successfully.")
        return True

    def modify_professor_details(self, professor_id, **kwargs):
        professors = read_csv(self.FILE_PATH)
        found = False

        for professor in professors:
            if professor["professor_id"] == professor_id:
                for key, value in kwargs.items():
                    if key in professor:
                        professor[key] = str(value)
                found = True
                break

        if not found:
            print("Professor not found.")
            return False

        write_csv(self.FILE_PATH, professors, self.HEADERS)
        print("Professor updated successfully.")
        return True

    def show_course_details_by_professor(self, professor_id):
        professors = read_csv(self.FILE_PATH)
        for professor in professors:
            if professor["professor_id"] == professor_id:
                print(f"Professor: {professor['name']}")
                print(f"Course ID: {professor['course_id']}")
                return professor
        print("Professor not found.")
        return None
