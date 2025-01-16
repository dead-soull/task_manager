<<<<<<< Updated upstream
test = 123
test1 = 321
test2 = 133
=======
import json

ver = "0.0.1"
def greetings():
    name = input("What's your name?\n")
    print(f'Hello, {name}. Welcome to the Task Manager {ver}!')

def newTask():
    taskName = input("What do you want to schedule?\n")
    print('Information saved!')

def main():
    print("=== Welcome to My First CLI Task Manager ===")
    greetings()
    newTask()
    

if __name__ == "__main__":
    main()
>>>>>>> Stashed changes
