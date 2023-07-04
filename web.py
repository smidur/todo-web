import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state['new_todo']
    todo = todo.strip()
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""

st.title('To-Do App')
st.subheader('This is To-Do App')
st.write("This app is to increase your productivity")

st.text_input(label="text_input_label", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st._rerun()
