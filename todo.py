# ============================
# Advanced To-Do List App
# Author: Soham Patil
# ============================

import json
from datetime import datetime

FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks available.\n")
        return

    print("\n📝 Your Tasks:")
    for i, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "⏳ Pending"
        print(
            f"{i}. {task['title']} | "
            f"Priority: {task['priority']} | "
            f"{status} | "
            f"Added: {task['timestamp']}"
        )
    print()


def add_task(tasks):
    title = input("Enter task title: ").strip()
    if not title:
        print("⚠ Task title cannot be empty.")
        return

    priority = input("Priority (Low/Medium/High): ").capitalize()
    if priority not in ["Low", "Medium", "High"]:
        priority = "Low"

    task = {
        "title": title,
        "priority": priority,
        "completed": False,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    tasks.append(task)
    print("✅ Task added successfully!")


def mark_task_done(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("🎉 Task marked as completed!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def remove_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return

    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑 Removed task: {removed['title']}")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Save & Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Tasks saved. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please select 1–5.")


if __name__ == "__main__":
    main()
