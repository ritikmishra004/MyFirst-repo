import os

def show_tasks(tasks):
    if not tasks:
        print("no tasks to show")
    else:
        print("Your To-Do list is: ")
        for index,task in enumerate(tasks,start=1):
            print(f"{index}. {task}")

            '''(Yeh enumerate() ka use aapko tasks ko display karte 
            waqt har task ke sath uska index print karne mein madad karta hai.)'''

def add_task(tasks):
    task= input("enter the task you want to add: ")
    tasks.append(task)
    print(f"task {tasks} added")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        tasks_num= int(input("enter the no.of tasks you waht to remove"))
        if 1<= tasks_num <= len(tasks):
            removed_task= tasks.pop(tasks_num-1)
            print(f"task '{removed_task}' removed")
        else :
            print("invalid tasks")
    except ValueError:
        print("please enter a valid number")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        tasks_num=int(input("enter the no of tasks mark as completed"))
        if 1<= tasks_num <= len(tasks):
            tasks[tasks_num-1]+= "(completed)"
            print(f"tasks '{tasks[tasks_num]}' completed")
        else:
            print("invalid task no.")
    except:
        print("enter valid number")

def todo_app():
    tasks=[]

    while True:
        print("\n To-Do list:")
        print("1. show tasks")
        print("2. add tasks")
        print("3. remove tasks")
        print("4. mark as complete")
        print("5. exit")

        choice= input("enter any no. ")

        if choice == '1':
            show_tasks(tasks)
        elif choice =='2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            complete_task(tasks)
        elif choice == '5':
            print("exiting the app")
            break
        else:
            print("invalid option please try again")

todo_app()