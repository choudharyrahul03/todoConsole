# python console application todo app
# todos = []
from functions import get_todo,write_todo
import functions
while True:
    user_action = input("Enter add, edit, delete, show or exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todos=functions.get_todo()
        todo = user_action[4:] + "\n"
        todos.append(todo)
        write_todo(todos)
    elif user_action.startswith('edit'):
        try:
            todo_number = int(user_action[5:])
            todo_number = todo_number - 1
            new_todo = input("Enter a new todo: ") + "\n"
            todos =functions.get_todo()
            todos[todo_number] = new_todo
            with open("todo.txt","w") as file:
                file.writelines(todos)
        except ValueError:
            print("Wrong Input, Enter todo number after edit!!")
            continue
    elif user_action.startswith('delete'):
        num = int(user_action[7:])
        num = num - 1
        todos = functions.get_todo()
        todos.pop(num)
        functions.write_todo(todos)
    elif user_action.startswith('show'):
        todos = get_todo()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('exit'):
        break
    else:
        print("Wrong input!!")
print("Good Bye!!")


