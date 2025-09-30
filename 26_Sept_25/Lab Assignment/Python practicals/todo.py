def todo_manager():
    """
    A simple To-Do List Manager.
    Allows user to:
    1. View todos
    2. Add todos
    3. Remove todos
    4. Mark todos as completed
    5. Exit the program
    """
    todos = []  # List to store todos (each todo is a dict with task & completed status)

    while True:
        # Menu Display
        print("\n=== TODO LIST MANAGER ===")
        print("1. View todos")
        print("2. Add todo")
        print("3. Remove todo")
        print("4. Mark todo as completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # ---- 1. VIEW TODOS ----
        if choice == "1":
            if not todos:
                print("\n No todos yet!")
            else:
                print("\nYour Todos:")
                for i, todo in enumerate(todos, 1):
                    status = "✓" if todo["completed"] else " "  # checkmark if completed
                    print(f"{i}. [{status}] {todo['task']}")

        # ---- 2. ADD TODO ----
        elif choice == "2":
            task = input("Enter new task: ")
            todos.append({"task": task, "completed": False})
            print(f"Added: {task}")

        # ---- 3. REMOVE TODO ----
        elif choice == "3":
            if not todos:
                print("\nNo todos to remove!")
                continue

            try:
                index = int(input("Enter todo number to remove: ")) - 1
                if 0 <= index < len(todos):
                    removed = todos.pop(index)
                    print(f"Removed: {removed['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        # ---- 4. MARK TODO AS COMPLETED ----
        elif choice == "4":
            if not todos:
                print("\nNo todos to mark!")
                continue

            try:
                index = int(input("Enter todo number to mark as completed: ")) - 1
                if 0 <= index < len(todos):
                    todos[index]["completed"] = True
                    print(f"Marked as completed: {todos[index]['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        # ---- 5. EXIT ----
        elif choice == "5":
            print("Goodbye! Have a productive day!")
            break

        # ---- INVALID CHOICE ----
        else:
            print("Invalid choice! Please enter 1-5.")

# Run the program
todo_manager()
