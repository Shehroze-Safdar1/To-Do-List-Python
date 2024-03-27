#This is simple command line to-do list made using python

def add_task(todo_list,task):
    todo_list.append(task)
    print("Task is added successfully")

def view_task(todo_list):
    if todo_list:
        print("Tasks present in to-do list are")
        for index,task in enumerate(todo_list,start=1):
            print(f"{index}.{task}")
    else:
        print("No task is present in to-do list!!")

def mark_completed(todo_list,task_index):
    if 1<=task_index <=len(todo_list):
        print(f"Task'{todo_list[task_index-1]}' marked as complete")
        del todo_list[task_index-1]

    else:
        print("Invalid task")

def remove_task(todo_list,task_index):
    if 1<=task_index <=len(todo_list):
        print(f"Task'{todo_list[task_index-1]}' removed")
        del todo_list[task_index-1]

    else:
        print("Invalid task!!")

def main():
    todo_list=[]
    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")

        choice=input("Enter your choice:")
        if choice== '1':
            task=input("Enter the task:")
            add_task(todo_list,task)
        elif choice == '2':
            view_task(todo_list)

        elif choice == '3':
            view_task(todo_list)
            task_index=int(input("Enter the index of task to mark as complete:"))
            mark_completed(todo_list,task_index)

        elif choice == '4':
            view_task(todo_list)
            task_index=int(input("Enter the index of task to remove the task:"))
            remove_task(todo_list,task_index)

        elif choice == '5':
            print("Exiting the program.///...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


