import json


def add_file(user):
    file = open("../1029/user.txt", "w",encoding="UTF-8")
    file.write(user)
    file.close()


def read_file():
    file = open("../1029/user.txt", "r",encoding="UTF-8")
    content = file.read()
    file.close()
    # print(f"content={content}")
    return content

