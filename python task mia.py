import json
import os
FILENAME="TODO_LIST.json"

def load_data(): # return the vlaues
     if os.path.exists(FILENAME):
         with open(FILENAME,"r", encoding="utf-8") as f :
             data = json.load(f)
             return data["tasks"] , data["statuses"]
     return[], []
def save_data(todo_list, status_list) :
        data ={
            "tasks":todo_list,
            "statuses":status_list
        }
        with open(FILENAME,"w" , encoding="utf-8") as f :
            json.dump(data,f,ensure_ascii=False, indent=4)

todo_list , status_list= load_data()

def greeting():
    print("\n Welcome to lighting McQueen's To-Do LIST\n" "HELLO McQueen's\n")
greeting()

while True:
    print("1.Add a task \n" "2.View my to-do list\n" "3.Mark a task as done\n" "4.Remove a task\n" "5.Quit\n")
    choice=input("What's the move, champ?: ")
    if choice=="1":
        task=input("Enter your task: ")
        todo_list.append(task)
        status_list.append (False) # by default 
        save_data(todo_list, status_list)
        print("task is added successfully\n")
    
    elif choice=="2":
        if len(todo_list)==0 :
           print("your list is empty")
        for i in range(len(todo_list)):
            if (status_list[i]) == True :
                status ="[Done]"
            else :
                status="[pending]"
            print (f"{i+1}. {todo_list[i]} {status}")  # num of task + task + status

    elif choice=="3":
        if len(todo_list)== 0 :
           print("no task found\n")
        else:   
           task_num=int (input("Enter the task number to mark as done: "))
           status_list[task_num - 1] = True
           save_data(todo_list, status_list)
           print("Task marked as done\n")
   
    elif choice=="4" :
        if len(todo_list)== 0 :
           print("no task to remove\n")
        else:
            task_num=int(input("enter number of task to remove"))
            remove=todo_list.pop(task_num-1)
            status_list.pop(task_num-1)
            save_data(todo_list, status_list)
            print(f"Removed:'{remove}'\n")

    elif choice=="5":
         save_data(todo_list, status_list)
         print("see you at the end")
         break


        
 