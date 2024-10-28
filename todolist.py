todo_list = []

def add_todo(todo_item):
  todo_list.append(todo_item)
  print(f"Added TODO: {todo_item}")

def show_todos():
    if not todo_list:
      print("No TODOs found.")
    else:
      print("TODO List:")
      for i, todo in enumerate(todo_list, 1):
        print(f"{i}. {todo}")

def delete_todo(todo_item):
  if 0 <= index < len(todo_list):
    removed_todo = todo_list.pop(index)
    print(f"Delete TODO: {removed_todo}")
  else:
    print("Invalid index. Plese enter a valid TODO number.")

while True:
  print("/nSelect an option:")
  print("1. Add TODO")
  print("2. Show TODOs")
  print("3. Delete TODO")
  print("4. Exit")

  choice = input("Enter yuour choice (1/2/3/4):")

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
    print("Exiting TODO List App.")
    break
  else:
    print("invalid choice. Please enter 1, 2, 3, or 4.")