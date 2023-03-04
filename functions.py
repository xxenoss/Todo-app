Filepath = 'todos.txt'


def Read_files(filepath=Filepath):
    files = open(filepath, "r")
    reading_todos = files.readlines()
    return reading_todos


def Write_files(todos, filepath=Filepath):
    files = open(filepath, 'w')
    files.writelines(todos)
