import PySimpleGUI as sg
from functions import Write_files, Read_files

# Creating layout for the window
layout = [
    [sg.Text("Tpe a TODO")],
    [sg.InputText(tooltip='Enter todo', key='input_todo'), sg.Button("ADD")],
    [sg.Button("Edit"), sg.Button("Delete")],
    [sg.Listbox(values=Read_files(), key="listbox", size=(50, 20), enable_events=True, )]
]
# Display window
window = sg.Window("My TODO App", layout=layout)

while True:
    event, values = window.read()
    # ADD todos
    if event == "ADD":
        todos = Read_files()
        add_todo = values["input_todo"] + "\n"
        todos.append(add_todo)
        Write_files(todos)
        window["listbox"].update(values=todos)
    # Update the listbox
    elif event == "listbox":
        window["input_todo"].update(value=values["listbox"][0])
        # Edit todos
    elif event == "Edit":
        todos = Read_files()
        new_todos = values["input_todo"] + "\n"
        todo_to_edit = values["listbox"][0]
        index = todos.index(todo_to_edit)
        todos[index] = new_todos
        Write_files(todos)
        window["listbox"].update(todos)
        # Delete todos
    elif event == "Delete":
        todos = Read_files()
        selected_todo = values["listbox"][0]
        index = todos.index(selected_todo)
        todos.pop(index)
        window["listbox"].update(values=todos)
        Write_files(todos)
    # Exiting the programme

    elif event == sg.WIN_CLOSED:
        break
window.close()
