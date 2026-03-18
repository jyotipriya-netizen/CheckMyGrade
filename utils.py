import csv
import os
import time
import base64


def ensure_file_exists(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()


def read_csv(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(file_path, data, headers):
    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)


def append_csv(file_path, row, headers):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        if not file_exists or os.path.getsize(file_path) == 0:
            writer.writeheader()
        writer.writerow(row)


def search_with_time(records, key, value):
    start_time = time.perf_counter()
    results = [record for record in records if record.get(key, "").lower() == value.lower()]
    end_time = time.perf_counter()
    elapsed = end_time - start_time
    return results, elapsed


def generate_next_id(prefix, records, id_field):
    max_num = 0
    for record in records:
        record_id = record.get(id_field, "")
        if record_id.startswith(prefix):
            try:
                num = int(record_id[len(prefix):])
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
    return f"{prefix}{max_num + 1}"


def encrypt_password(password):
    encoded_bytes = base64.b64encode(password.encode("utf-8"))
    return encoded_bytes.decode("utf-8")


def decrypt_password(encoded_password):
    decoded_bytes = base64.b64decode(encoded_password.encode("utf-8"))
    return decoded_bytes.decode("utf-8")
