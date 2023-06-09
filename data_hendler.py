import csv
import os


DATA_FILE_PATH = (
    os.getenv("DATA_FILE_PATH") if "DATA_FILE_PATH" in os.environ else "data.csv"
)
QUESTION_HEADER = [
    "id",
    "submission_time",
    "view_number",
    "vote_number" "title",
    "message",
    "image",
    "user_id",
]

ANSWER_HEADER = [
    "id",
    "submission_time",
    "vote_number",
    "question_id",
    "message",
    "image",
    "user_id",
]


def addtofile(data, file):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)


def readfile(file):
    with open(file, "r") as f:
        return list(csv.DictReader(f))


def find_data_in_list(data, list, key):
    return_list = []
    for e in list:
        if str(data) == e[key]:
            return_list.append(e)
    return return_list


def read_specific_data(file, key, data):
    full_data = readfile(file)
    return_data = find_data_in_list(data, full_data, key)
    if return_data == []:
        return_data = None
    return return_data


def write_new_file(file, headers, list):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for dictionary in list:
            writer.writerow(dictionary.values())


def remove_data_from_list(list, data, key):
    return_list = []
    for e in list:
        if str(data) != e[key]:
            return_list.append(e)
    return return_list


def delete_data(file, data_to_delete, key, headers):
    old_file = readfile(file)
    new_file = remove_data_from_list(old_file, data_to_delete, key)
    write_new_file(file, headers, new_file)


def add_vote_in_list(list, data, key):
    return_list = []
    for e in list:
        if str(data) == e[key]:
            e["vote_number"] = int(e["vote_number"]) + 1
            e["vote_number"] = str(e["vote_number"])
        return_list.append(e)
    return return_list


def add_vote(file, data_to_delete, key, headers):
    old_file = readfile(file)
    new_file = add_vote_in_list(old_file, data_to_delete, key)
    write_new_file(file, headers, new_file)