from utils import read_csv, write_csv, append_csv, encrypt_password, decrypt_password


class LoginUser:
    FILE_PATH = "data/login.csv"
    HEADERS = ["user_id", "password", "role"]

    def register_user(self, user_id, password, role):
        users = read_csv(self.FILE_PATH)

        for user in users:
            if user["user_id"] == user_id:
                print("User already exists.")
                return False

        encrypted = encrypt_password(password)
        new_user = {
            "user_id": user_id,
            "password": encrypted,
            "role": role
        }

        append_csv(self.FILE_PATH, new_user, self.HEADERS)
        print("User registered successfully.")
        return True

    def login(self, user_id, password):
        users = read_csv(self.FILE_PATH)

        for user in users:
            if user["user_id"] == user_id:
                stored_password = decrypt_password(user["password"])
                if stored_password == password:
                    print("Login successful.")
                    return True
                print("Invalid password.")
                return False

        print("User not found.")
        return False

    def logout(self):
        print("Logout successful.")

    def change_password(self, user_id, new_password):
        users = read_csv(self.FILE_PATH)
        found = False

        for user in users:
            if user["user_id"] == user_id:
                user["password"] = encrypt_password(new_password)
                found = True
                break

        if not found:
            print("User not found.")
            return False

        write_csv(self.FILE_PATH, users, self.HEADERS)
        print("Password changed successfully.")
        return True
