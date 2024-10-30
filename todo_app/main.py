from todolist import add_todo, show_todos, delete_todo, change_status, deadline_todo

#メインプログラム
while True:
  print("/nSelect an option:")
  print("1. Add TODO")
  print("2. Show TODOs")
  print("3. Delete TODO")
  print("4. Change Status to Done")
  print("5. Change the deadline")
  print("6. Exit")

  choice = input("Enter yuour choice (1~6):")

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
    show_todos()
    try:
      index = int(input("Enter the TODO number to change the deadline:")) - 1
      new_deadline = input("Enter the new TODO deadline(YYYY-MM-DD):")
      deadline_todo(index, new_deadline)
    except ValueError:
      print("Plese enter a valid number.")
  elif choice == '6':
    print("Exiting TODO List App.")
    break
  else:
    print("invalid choice. Please enter 1, 2, 3, 4, 5,or 6.")