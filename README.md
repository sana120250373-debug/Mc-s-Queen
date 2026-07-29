What is the target of this code?
The main target is to build a ToDo List application for McQueen
​Is a To-Do List just about writing tasks down?
No it has multiple features: I can add a task, delete a task, view all tasks, and check whether a task is completed or still pending
​How does the code work step-by-step?
​Greeting Message:
First, I display a welcome message using a function that I call which is responsible for printing the greeting
​Then we have a menu to start editing in this todo list
I present a menu to let the user choose what action they want to take in the To-Do List through take from the user's input  number to determine his choice
​Handling Menu Choices depending on the user's choice we have 5 choices
​Option 1 (Add a task): i add new task through i append a new task to the task list and set its status to pending by default
​Option 2 (View tasks): I display all existing tasks using a for loop that iterates through each task and checks its status whether it is done or pending to print it clearly.
​Option 3 (Mark as done): The user informs me that a specific number of the task is completed I take the task number from the user and update its status to True (Done)
​Option 4 (Remove a task): I delete a task by taking its number from the user and removing it from the list
​Option 5 (Quit): I exit the program loop "break"

How did we save the output into a file?
We used JSON, which allows us to store and structure the data so the program can easily read and write it without losing information when closed
​How does JSON handling work in our code?
It is divided into two main processes
​load_data() (Loading Data): What it does it checks if the JSON file exists on the computer
If it exists it reads the stored data and loads it back into our Python lists so McQueen can see his previous tasks if the file doesn't exist yet it simply starts with empty lists
​save_data() (Saving Data): 
​What it does: It takes our current task list and status list, packs them together into a dictionary converts them into JSON format 
and writes them into the file we call this function after any change adding, updating or deleting a task to make sure every modification is saved instantly
