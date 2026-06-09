# ==================================================
# Todo List CLI
# ==================================================
# A command-line todo list application built in Python.
#
# Features:
# - Add new tasks
# - View active tasks
# - Mark tasks as completed
# - Track completed tasks
# - Display a completion summary
#
# Skills Demonstrated:
# - Lists
# - Loops
# - User Input Handling
# - Conditional Logic
# - Input Validation
# ==================================================

header = """
  _____         _           
 |_   _|__   __| | ___  ___ 
   | |/ _ \ / _` |/ _ \/ __|
   | | (_) | (_| | (_) \__ \\
   |_|\___/ \__,_|\___/|___/
                            
"""

print(header)

# Store active and completed tasks
todos = []
completed = []

while True:
    # Display current todos
    print("\nCurrent Todos:")

    if todos:
        for i in range(len(todos)):
            print(f"{i + 1}) {todos[i]}")
    else:
        print("No todos yet.")

    print("*" * 40)
    print('Enter a todo, type its number to complete it, or type "Q" to quit:')

    command = input("> ").strip()

    # Exit program
    if command.lower() == "q":
        break

    # Complete a todo
    elif command.isnumeric():
        index = int(command) - 1

        if index >= len(todos):
            print("There is no todo with that number.")
        else:
            completed_todo = todos.pop(index)
            completed.append(completed_todo)
            print(f'Completed: "{completed_todo}"')

    # Add a new todo
    else:
        todos.append(command)
        print(f'Added: "{command}"')

# Print completion summary
if completed:
    print(f"\nYou completed {len(completed)} todos today:")

    for todo in completed:
        print(f"* {todo}")
else:
    print("\nYou did not complete any todos today.")

print("OK GOODBYE!")
