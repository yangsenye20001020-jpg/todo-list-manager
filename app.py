# Simple To-Do List Manager

tasks = []

def add_task(task):
    tasks.append(task)

def list_tasks():
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

if __name__ == "__main__":
    add_task("Buy milk")
    add_task("Study Python")
    list_tasks()
