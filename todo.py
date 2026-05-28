
import json
tasks = []
def save_tasks():
    print("Saving: " + str(tasks))
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []        
def complete_task():
    print("what is the task num you want to complete? ")
    task_num = int(input())
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
    else:
        print("Invalid task number.")
def printmenu():
    print("What would you like to do?")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    print("5. Mark a task as completed")

def remove_task():
    print("what is the task num you want to remove? ") 
    task_num = int(input())
    if 0 < task_num <= len(tasks):
        tasks.pop(task_num - 1)
    else:
        print("Invalid task number.")
        #    
def add_task(task):
    tasks.append({"task": task, "completed": False})
    print("Task added: " + task)
    #
def view_tasks():
     if len(tasks) == 0:
        print("Your list is empty!")
        return
     else:
        sorted_tasks = sorted(tasks, key=lambda t: t["completed"] == True)
        for i in range(len(sorted_tasks)):
         print(str(i+1) + ". " + sorted_tasks[i]["task"] + " - " + ("Completed" if sorted_tasks[i]["completed"] else "Not Completed"))
print("Welcome to the To-Do List App!")
load_tasks()

while True:
    printmenu()
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        add_task(task)
    elif choice == "2":
        print("Your tasks:")
        view_tasks()
    elif choice == "3":
       remove_task()
    elif choice == "4":
        print("Goodbye!")
        save_tasks()
        break
    elif choice == "5":
        complete_task()
        print("Task marked as completed.")
    else:
        print("Invalid choice. Please try again.")
