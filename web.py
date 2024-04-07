import streamlit as st
from modules import functions

# Get the current list of to-do items
todos = functions.get_todos()

def add_todo():
    todo_to_add = st.session_state["todo_to_add"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)

st.title("Dan's ToDo App")
st.subheader("Increasing productivity one task at a time")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key="todo_to_add")