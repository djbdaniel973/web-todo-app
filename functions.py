# This is the BACK END of the coding.

# Define the absolute path to the todos.txt file
TODO_FILE = r"C:\Users\Mr. Purple\Documents\Software Engineering\All my projects\1st project\1. Todo App\todos.txt"

# Function to read todos from the file
# Returns a list of todos, each as a stripped string (no leading/trailing whitespace)
def get_todos():
    try:
        with open(TODO_FILE, "r") as file:
            todos = file.readlines()  # Read all lines from the file
            todos = [todo.strip() for todo in todos]  # Remove leading/trailing whitespace from each line
    except FileNotFoundError:
        todos = []  # Return an empty list if the file is not found
    return todos

# Function to write todos to the file
# Takes a list of todos and writes each one to the file, each on a new line
def write_todos(todos):
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(todo + "\n")  # Write each todo followed by a newline character
