todo_list = []

#新規TODOを追加する関数
def add_todo(todo_item):
  todo_list.append({"task": todo_item, "status": "todo"})
  print(f"Added TODO: {todo_item}")
  print(f"Current TODO List: {todo_list}")

#追加済TODOを表示する関数
def show_todos():
    if not todo_list:
      print("No TODOs found.")
    else:
      print("TODO List:")
      for i, todo in enumerate(todo_list, 1):
        print(f"{i}. {todo['task']} - Status: {todo['status']}")

#TODOのステータスを変更する関数
def change_status(index):
  if 0 <= index < len(todo_list):
    todo_list[index]["status"] =  "done"
    print(f"Status of TODO: '{todo_list[index]['task']}' changed to 'done'")
  else:
    print("Invalid index. Plese enter a valid TODO number.")

#TODOを削除する関数
def delete_todo(todo_item):
  if 0 <= index < len(todo_list):
    removed_todo = todo_list.pop(index)
    print(f"Delete TODO: {removed_todo['task']}")
  else:
    print("Invalid index. Plese enter a valid TODO number.")

#メインプログラム
while True:
  print("/nSelect an option:")
  print("1. Add TODO")
  print("2. Show TODOs")
  print("3. Delete TODO")
  print("4. Change Status to Done")
  print("5. Exit")

  choice = input("Enter yuour choice (1/2/3/4/5):")

  if choice == '1':
    new_todo = input("Enter the new TODO:")
    add_todo(new_todo)
  elif choice == '2':
    show_todos()
  elif choice == '3':
    show_todos()
    try:
      index = int(input("Enter the TODO number to delete: ")) - 1
      delete_todo(index)
    except ValueError:
      print("Plese enter a valid number.")
  elif choice == '4':
    show_todos()
    try:
      index = int(input("Enter the TODO number to mark as done:")) - 1
      change_status(index)
    except ValueError:
      print("Plese enter a valid number.")
  elif choice == '5':
    print("Exiting TODO List App.")
    break
  else:
    print("invalid choice. Please enter 1, 2, 3, 4, or 5.")