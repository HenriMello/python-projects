todo_list = []

while True:
  if not todo_list:
    print("Your ToDo list is empty")
  else:
    index = 1
    for task in todo_list:
      print(f"{index}. {task}")
      index += 1

  print("Options:")
  print("1. Add Task")
  print("2. Remove Task")
  print("3. Quit")

  choice = input("Enter your choice (1, 2, or 3): ")

  if choice == "1":
    print("Adding task")
    new_task = input("Enter the task: ")
    todo_list.append(new_task)
    print(f"Task '{new_task}' added to the ToDo list")
  elif choice == "2":
    if len(todo_list) > 0:
      print("Removing task")
      removed_task = todo_list.pop()
    else:
      print("Your ToDo list is empty")
  elif choice == "3":
    print("Quitting")
    break