import reflex as rx
from typing import List

class Todo(rx.Base):
    text: str
    completed: bool = False

class State(rx.State):
    """The app state."""
    todos: List[Todo] = []
    new_todo: str = ""

    def add_todo(self):
        if self.new_todo.strip():
            self.todos.append(Todo(text=self.new_todo))
            self.new_todo = ""

    def toggle_todo(self, index: int):
        self.todos[index].completed = not self.todos[index].completed

    def delete_todo(self, index: int):
        self.todos.pop(index)

def todo_item(todo: Todo, index: int):
    return rx.hstack(
        rx.checkbox(
            is_checked=todo.completed,
            on_change=State.toggle_todo(index),
        ),
        rx.text(
            todo.text,
            text_decoration="line-through" if todo.completed else "none",
            flex="1",
        ),
        rx.button(
            "×",
            on_click=State.delete_todo(index),
            color="red",
            bg="transparent",
            border="none",
        ),
        width="100%",
        padding="2",
        border_bottom="1px solid #eee",
    )

def index():
    return rx.vstack(
        rx.heading("Todo List"),
        rx.hstack(
            rx.input(
                placeholder="Add a new task...",
                value=State.new_todo,
                on_change=State.set_new_todo,
            ),
            rx.button("Add", on_click=State.add_todo),
        ),
        rx.vstack(
            rx.foreach(
                State.todos,
                lambda todo, index: todo_item(todo, index)
            )
        ),
        padding="2em",
    )

app = rx.App()
app.add_page(index)
