"""A simple todo app."""

import reflex as rx

class Task(rx.Base):
    """A task."""
    text: str
    done: bool = False


class State(rx.State):
    """The app state."""
    tasks: list[Task] = []
    new_task: str = ""

    def add_task(self):
        """Add a new task."""
        if self.new_task:
            self.tasks.append(Task(text=self.new_task))
            self.new_task = ""

    def delete_task(self, idx: int):
        """Delete a task."""
        self.tasks.pop(idx)

    def toggle_done(self, idx: int):
        """Toggle a task done."""
        self.tasks[idx].done = not self.tasks[idx].done


def index() -> rx.Component:
    """The main view."""
    return rx.center(
        rx.vstack(
            rx.heading("Todo App", font_size="2em"),
            rx.hstack(
                rx.input(
                    placeholder="Add a task",
                    value=State.new_task,
                    on_change=State.set_new_task,
                ),
                rx.button("Add", on_click=State.add_task),
                width="100%",
            ),
            rx.divider(),
            rx.vstack(
                rx.foreach(
                    State.tasks,
                    lambda task, idx: rx.hstack(
                        rx.checkbox(
                            on_change=lambda: State.toggle_done(idx),
                            is_checked=task.done,
                        ),
                        rx.text(
                            task.text,
                            decoration_line="line-through" if task.done else "none",
                        ),
                        rx.button(
                            "Delete",
                            on_click=lambda: State.delete_task(idx),
                            size="sm",
                        ),
                        width="100%",
                    ),
                ),
                width="100%",
                padding="1em",
            ),
            width="100%",
            max_width="600px",
            padding="2em",
        )
    )


# Create the app and add the state.
app = rx.App()
app.add_page(index)
