

import os # Used to check if the tasks file exists

# Define the filename for storing tasks
FILENAME = "tasks.txt"

def load_tasks():

    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r') as file:
        # Read each line and strip the newline character from the end
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
   
    with open(FILENAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def view_tasks(tasks):
   
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("Your to-do list is empty. Great job! ")
    else:
        # Enumerate adds a counter to an iterable
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    print("--------------------------\n")

def add_task(tasks):
    
    task = input("Enter the new task: ")
    if task: # Make sure the user entered something
        tasks.append(task)
        save_tasks(tasks)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty.")

def remove_task(tasks):
    
    view_tasks(tasks) # Show tasks first so the user can pick one
    if not tasks:
        return # Can't remove from an empty list

    try:
        task_num_str = input("Enter the number of the task to remove: ")
        if not task_num_str:
            print("No task number entered.")
            return

        task_num = int(task_num_str)
        # Check if the number is valid
        if 1 <= task_num <= len(tasks):
            # Adjust for 0-based index by subtracting 1
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number. Please enter a number from the list.")
    except ValueError:
        # Catches the error if the user enters text instead of a number
        print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the To-Do List Manager!")
    # Load tasks from the file when the application starts
    tasks = load_tasks()

    while True:
        # Display the main menu
        print("\n===== TO-DO LIST MENU =====")
        print("1. View Tasks")
        print("2. Add a Task")
        print("3. Remove a Task")
        print("4. Exit")
        print("===========================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye! Keep up the great work! ")
            break
        else:
            print(" Invalid choice. Please enter a number between 1 and 4.")

# This standard Python construct ensures that main() runs only when
# the script is executed directly.
if __name__ == "__main__":
    main()