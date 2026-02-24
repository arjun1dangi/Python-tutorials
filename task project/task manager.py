import json
import os

TASK_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    """Add a new task."""
    title = input("Enter task title: ")
    description = input("Enter description: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    
    tasks = load_tasks()
    task_id = len(tasks) + 1
    tasks.append({
        "id": task_id,
        "title": title,
        "description": description,
        "deadline": deadline,
        "status": "Pending"
    })
    
    save_tasks(tasks)
    print("✅ Task added successfully!")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("⚠ No tasks found.")
        return

    print("\n📌 **Task List**")
    print("-" * 40)
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Status: {task['status']}")
        print("-" * 40)

def update_task():
    """Update task status."""
    tasks = load_tasks()
    if not tasks:
        print("⚠ No tasks to update.")
        return

    view_tasks()
    task_id = int(input("Enter task ID to update: "))
    for task in tasks:
        if task["id"] == task_id:
            print("\nSelect new status:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")
            choice = int(input("Enter choice: "))

            status_map = {1: "Pending", 2: "In Progress", 3: "Completed"}
            task["status"] = status_map.get(choice, "Pending")

            save_tasks(tasks)
            print("✅ Task updated successfully!")
            return

    print("⚠ Task ID not found!")

def delete_task():
    """Delete a task."""
    tasks = load_tasks()
    if not tasks:
        print("⚠ No tasks to delete.")
        return

    view_tasks()
    task_id = int(input("Enter task ID to delete: "))
    tasks = [task for task in tasks if task["id"] != task_id]

    save_tasks(tasks)
    print("✅ Task deleted successfully!")

def main():
    """Main function to run the task manager."""
    while True:
        print("\n📌 Welcome to Task Manager!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
