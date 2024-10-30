from datetime import datetime

todo_list = []

#新規TODOを追加する関数
def add_todo(todo_item):
  todo_list.append({"task": todo_item, "status": "todo", "deadline": "none"})
  print(f"Added TODO: {todo_item}")
  print(f"Current TODO List: {todo_list}")

#追加済TODOを表示する関数
def show_todos():
    if not todo_list:
      print("No TODOs found.")
    else:
      print("TODO List:")
      for i, todo in enumerate(todo_list, 1):
        print(f"{i}. {todo['task']} - Status: {todo['status']} - Deadline: {todo['deadline']}")

#TODOのステータスを変更する関数
def change_status(index):
  if 0 <= index < len(todo_list):
    todo_list[index]["status"] =  "done"
    print(f"Status of TODO: '{todo_list[index]['task']}' changed to 'done'")
  else:
    print("Invalid index. Plese enter a valid TODO number.")

#TODOを削除する関数
def delete_todo(index):
  if 0 <= index < len(todo_list):
    removed_todo = todo_list.pop(index)
    print(f"Delete TODO: {removed_todo['task']}")
  else:
    print("Invalid index. Plese enter a valid TODO number.")

#TODOの期日を入力する関数
def deadline_todo(index, new_deadline):
  if 0 <= index < len(todo_list):
    try:
      todo_list[index]["deadline"] = datetime.strptime(new_deadline, "%Y-%m-%d")
      print(f"Deadline of TODO: '{todo_list[index]['task']}' changed to '{new_deadline}'")
    except ValueError:
      print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
  else:
    print("Invalid index. Plese enter a valid TODO number.")
