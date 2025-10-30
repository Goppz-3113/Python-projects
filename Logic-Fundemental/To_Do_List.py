#To-Do-List

tasks=[] #empty list to store the data

while True:
    print("==== To-Do-List===")
    print("1: View Tasks")
    print("2: Add Tasks")
    print("3: Remove Tasks")
    print("4: EXIT") 
    
    choice=int(input("Enter Your Choice: "))

    if choice==1:
        if len(tasks)==0:
            print("No Tasks Yet")
        else:
            print("Your tasks: ")
            for i, task in enumerate(tasks,start=1):
                print(f"{i}.{task}")

    elif choice==2:
        new_task=input("Enter the new task")
        tasks.append(new_task)
        print(f"Task{new_task} is added")

    elif choice==3:
        if len(tasks)==0:
            print("No tasks to remove")
        else:
            for i, task in enumerate(tasks,start=1):
              print(f"{i}.{task}")
            remove_task=int(input("Enter the task number to remove: "))
            if 1<= remove_task<= len(tasks):
                removed=tasks.pop(remove_task-1) # we should minus one from th euser input because the index of list starts from zero
                print(f"{removed}is removed from the list")
            else:
                print('Invalid Task')
    elif choice==4:
        break

    else:
        print("Invalid choice, please enter number between 1-4")