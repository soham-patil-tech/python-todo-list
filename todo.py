# ============================
# Simple To-Do List App
# Author: Soham Patil
# ============================

from datetime import datetime


def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        tasks.append(f"{task} ({timestamp})")
        print("✅ Task added with timestamp!")
    else:
        print("⚠ Task cannot be empty.")


def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"🗑 Removed: {removed_task}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save & Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select 1–4.")


if __name__ == "__main__":
    main()
