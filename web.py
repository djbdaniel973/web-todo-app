# This is a web app
import functions
import streamlit as st

# This code opens the web app:
# streamlit run "C:/Users/Mr. Purple/Documents/Software Engineering/Web App/web.py"
# cd "C:/Users/Mr. Purple/Documents/Software Engineering/Web App/web.py"
# cd "C:\Users\Mr. Purple\Documents\Software Engineering\Web App\web.py"

# Use the absolute path to your todos.txt file
todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"]
    if new_todo and new_todo not in todos:  # Prevent adding duplicates
        todos.append(new_todo)
        functions.write_todos(todos)
        st.session_state["new_todo"] = ""  # Clear input after adding

st.title("My Todo App")
st.subheader("Welcome to the Todo App")
st.write("This app is to increase your productivity.")

# Create a unique checkbox for each todo item
# We need to iterate over a copy of the list to avoid modifying it while iterating
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{i}")
    if checkbox:
        # Remove the todo item from the list
        todos.remove(todo)
        functions.write_todos(todos)
        st.rerun()  # Refresh the app state

# Input field for adding new todos
st.text_input(label="Add new todo: ", placeholder="Add new todo",
              on_change=add_todo, key="new_todo")
