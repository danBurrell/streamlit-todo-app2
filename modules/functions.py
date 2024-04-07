from pathlib import Path

TODO_FILEPATH = "todo.txt"

def get_todos(filepath=TODO_FILEPATH):
    """
    Reads to-do list from text file and returns list of to-do items.
    :param filepath: String
    :return todo_list: List
    """
    with open(filepath, 'r') as file_local:
        todo_list = file_local.readlines()
    return todo_list


def write_todos(todo_list, filepath=TODO_FILEPATH):
    """
    Writes a list of to do items to a text file.
    :param todo_list: list
    :param filepath: string
    :return: None
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_list)
    return None


def display_todos(todo_list):
    for index, item in enumerate(todo_list):
        item = item.strip('\n')
        print(f"{index + 1}-{item}")
    return None