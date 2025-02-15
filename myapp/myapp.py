import reflex as rx
from dataclasses import dataclass
from typing import List

@dataclass
class Todo:
    text: str
    completed: bool = False

class TodoState(rx.State):
    todos: List[Todo] = []
    new_todo: str = ""

    def add_todo(self):
        if self.new_todo.strip():
            self.todos.append(Todo(self.new_todo))
            self.new_todo = ""

    def toggle_todo(self, index: int):
        self.todos[index].completed = not self.todos[index].completed

    def delete_todo(self, index: int):
        self.todos.pop(index)

def todo_item(todo: Todo, index: int):
    return rx.hstack(
        rx.checkbox(
            is_checked=todo.completed,
            on_change=TodoState.toggle_todo(index),
        ),
        rx.text(
            todo.text,
            text_decoration="line-through" if todo.completed else "none",
            flex="1",
        ),
        rx.button(
            "×",
            on_click=TodoState.delete_todo(index),
            color="red",
            bg="transparent",
            border="none",
            _hover={"opacity": 0.8},
        ),
        width="100%",
        padding="2",
        border_bottom="1px solid #eee",
    )

def todo_list():
    return rx.vstack(
        rx.heading("Todo List", size="lg", margin_bottom="4"),
        
        rx.hstack(
            rx.input(
                placeholder="Add a new task...",
                value=TodoState.new_todo,
                on_change=TodoState.set_new_todo,
                width="100%",
                padding="2",
                border="1px solid #ddd",
                border_radius="md",
            ),
            rx.button(
                "Add",
                on_click=TodoState.add_todo,
                bg="blue.500",
                color="white",
                padding="2",
                border_radius="md",
                _hover={"bg": "blue.600"},
            ),
            width="100%",
        ),
        
        rx.vstack(
            rx.foreach(
                TodoState.todos,
                lambda todo, index: todo_item(todo, index)
            ),
            width="100%",
            margin_top="4",
            bg="white",
            border_radius="md",
            border="1px solid #ddd",
            padding="2",
        ),
        
        rx.text(
            f"Total tasks: {len(TodoState.todos)}",
            margin_top="4",
            color="gray.500",
        ),
        
        width="100%",
        max_width="600px",
        margin="auto",
        padding="4",
    )

app = rx.App()
app.add_page(todo_list)
